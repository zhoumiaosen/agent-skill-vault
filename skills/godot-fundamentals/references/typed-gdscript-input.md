# Typed GDScript and Input

## Match the Existing Language Level

Inspect neighboring scripts before changing style. In a typed Godot 4.x project, prefer explicit public contracts and inferred obvious locals:

```gdscript
class_name Countdown
extends Node

@export_range(0.0, 60.0, 0.1) var duration: float = 3.0
var _remaining: float = 0.0

func restart() -> void:
	_remaining = duration

func seconds_left() -> float:
	return _remaining

func _process(delta: float) -> void:
	_remaining = maxf(0.0, _remaining - delta)
```

Useful conventions:

- Type exported properties, member variables, parameters, and return values.
- Infer locals with `:=` when the expression has an unambiguous type.
- Use `StringName` values, including `&"action_name"`, for repeatedly used engine identifiers.
- Use `Array[SomeType]` when every entry follows one contract.
- Cast `instantiate()` and generic node lookups before relying on a custom API.
- Do not silence a type mismatch with a cast unless runtime failure is handled.
- Prefix private implementation members with `_` when that matches the project.

## Inspect the Input Map First

Read the `[input]` section of `project.godot` or inspect Project Settings > Input Map. Record:

- Existing action names and naming style.
- Keyboard, mouse, controller, and touch bindings.
- Deadzones for analog actions.
- Built-in `ui_*` actions already used by `Control` focus navigation.
- Any rebinding system that owns configuration at runtime.

Add semantic actions such as `interact`, `dash`, or `camera_zoom_in`; do not encode a device in the action name. Avoid replacing a binding merely because another key seems more conventional.

## Choose the Input Path

Use polling for state that remains active while held:

```gdscript
func movement_axis() -> Vector2:
	return Input.get_vector(
		&"move_left", &"move_right", &"move_up", &"move_down"
	)
```

Use `_unhandled_input()` for discrete gameplay actions that should happen only if UI did not consume the event:

```gdscript
func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed(&"interact"):
		_try_interact()
		get_viewport().set_input_as_handled()
```

Use these callbacks intentionally:

- `_input(event)`: earliest general input hook; reserve it for systems that must see events before normal handling.
- `Control._gui_input(event)`: input addressed to a specific UI control.
- `_unhandled_key_input(event)`: unhandled keyboard events only.
- `_unhandled_input(event)`: gameplay events after GUI and earlier handlers.
- `Input.is_action_pressed()`: current action state, useful for continuous control.
- `Input.is_action_just_pressed()`: one-frame transition, useful when an event object is not needed.

Do not mix several paths for one action without documenting which layer consumes it.

## Apply Time Correctly

Rates such as rotation, regeneration, and non-physics translation should use `delta`:

```gdscript
@export var turn_rate: float = 2.5

func _process(delta: float) -> void:
	rotation += Input.get_axis(&"turn_left", &"turn_right") * turn_rate * delta
```

For a `CharacterBody2D`, assign velocity in units per second and call `move_and_slide()` from `_physics_process()`:

```gdscript
func _physics_process(_delta: float) -> void:
	velocity = movement_axis() * speed
	move_and_slide()
```

Multiplying that velocity by `delta` makes the body much slower and applies time twice.

## Handle Missing Configuration

When code is meant to be portable across scenes, fail clearly:

```gdscript
func _ready() -> void:
	assert(InputMap.has_action(&"interact"), "Input action 'interact' is required.")
```

Use assertions for developer invariants, not user-facing recovery. If an exported reference is optional, branch safely and document the degraded behavior.

## Input Verification

- Exercise every action with each configured device.
- Test opposite directions and diagonal input.
- Test keyboard focus inside text fields and buttons.
- Confirm paused nodes receive or ignore input according to `process_mode`.
- Confirm one press produces one discrete action.
- Confirm remapped controls, if present, update without script changes.
- Check that UI actions do not also trigger gameplay underneath a menu.
