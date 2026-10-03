---
name: godot-fundamentals
description: "Godot 4.x nodes, scenes, resources, Input Map, project setup, and editor workflow. Use when creating or repairing foundational Godot projects, composing scene trees, instantiating PackedScenes, defining custom Resources, configuring input actions, or debugging node lifecycle and project settings."
license: MIT
metadata:
  author: godot-skills
  version: "1.0.0"
---

# Godot Fundamentals

Build on the project's existing Godot conventions instead of imposing a starter-project layout.

## Scope

Use this skill for:

- Choosing and arranging `Node`, `Node2D`, `Node3D`, and `Control` descendants.
- Creating reusable scenes and instantiating `PackedScene` resources.
- Defining and assigning built-in or custom `Resource` data.
- Adding typed GDScript to scene nodes and using lifecycle callbacks correctly.
- Configuring named input actions and selecting an input callback.
- Working with the Scene, FileSystem, Inspector, Output, Debugger, and Remote scene tree.
- Diagnosing basic project, import, node-path, transform, and scene-run problems.

Do not use this skill to introduce SOLID refactors, event architectures, commands, or object pools; use the programming-patterns skill. Do not use it to decide global state ownership, manager lifetimes, scene routing, or save boundaries; use the game-architecture skill. Keep genre-specific gameplay and advanced rendering out of scope.

## Inspect Before Editing

1. Locate `project.godot`; do not assume the current directory is the project root.
2. Read `config/features` and existing tooling to determine the exact Godot 4.x version. Avoid APIs introduced after that version.
3. Inspect `[application]`, `[autoload]`, `[input]`, `[display]`, and relevant `[rendering]` settings before changing project configuration.
4. Inspect nearby `.gd`, `.tscn`, `.tres`, and `.res` files. Match folder layout, naming, indentation, static-typing level, node naming, and signal-connection style.
5. Map the affected scene tree: root type, parent-child ownership, instantiated subscenes, editable children, exported references, unique-name nodes, and local versus global transforms.
6. Find the project's normal run, test, lint, and formatting commands. Run a baseline when practical.
7. Never edit generated `.godot/` import/cache contents. Change source assets or import settings instead.

If there is no `project.godot`, ask whether to initialize a project before creating Godot-specific files.

## Implementation Workflow

1. State the behavior in one observable sentence.
2. Select the narrowest built-in node whose behavior matches the requirement.
3. Decide whether the unit is a node, a reusable scene, or data in a resource.
4. Build the scene hierarchy before writing code that depends on it.
5. Expose designer-owned values with typed `@export` properties; cache stable child references with typed `@onready` properties.
6. Use named Input Map actions rather than physical key constants.
7. Implement the smallest typed script that completes the behavior.
8. Test the edited scene in isolation, then run the project entry scene.

## Core Decisions

### Nodes and scenes

- Choose by behavior first: a visible texture does not automatically make the root a `Sprite2D`, and a clickable object does not automatically need a physics body.
- Use `Node2D` for a transformable 2D grouping root, `Node3D` for 3D, `Control` for layout-driven UI, and plain `Node` for non-spatial coordination local to a scene.
- Make a scene when a node branch has an independent identity, is reused, or benefits from isolated testing.
- Let the nearest scene owner add and remove runtime children. Avoid attaching ordinary gameplay nodes directly to `SceneTree.root`.
- Add an instance to the tree before assigning a world-space transform that depends on its parent.
- Prefer `queue_free()` during normal scene-tree callbacks. Treat every stored node reference as invalid after its owner is freed.

```gdscript
extends Node2D

@export var pickup_scene: PackedScene
@onready var pickups: Node2D = %Pickups

func spawn_pickup(at: Vector2) -> void:
	if pickup_scene == null:
		push_error("Assign Pickup Scene before spawning a pickup.")
		return
	var pickup := pickup_scene.instantiate() as Node2D
	if pickup == null:
		push_error("The configured pickup scene must have a Node2D root.")
		return
	pickups.add_child(pickup)
	pickup.global_position = at
```

### Resources

- Use a resource for data that benefits from Inspector editing, reuse, or serialization independent of a live scene node.
- Use an external `.tres` when several scenes should share the same definition. Keep a built-in subresource when the data belongs only to one scene or resource.
- Assume resources are shared references. Do not put per-instance mutable state in a shared definition resource.
- Use `preload()` for a fixed dependency known when the script is parsed. Use `load()` or threaded loading only when the path is selected at runtime.
- Use stable identifiers in data that may later be persisted; display names and file paths are poor identities.

### Input and callbacks

- Poll held actions in `_physics_process()` for physics movement.
- Handle discrete gameplay events in `_unhandled_input()` when UI should get the first chance to consume them.
- Use `_process()` for frame-driven presentation that is not physics-dependent.
- Multiply manual rates by `delta`. Do not multiply `CharacterBody2D.velocity` by `delta` before `move_and_slide()` because velocity is already expressed per second.
- Prefix an intentionally unused callback argument with `_`.

```gdscript
extends CharacterBody2D

@export_range(0.0, 1200.0, 1.0) var speed: float = 240.0

func _physics_process(_delta: float) -> void:
	var direction := Input.get_vector(
		&"move_left", &"move_right", &"move_up", &"move_down"
	)
	velocity = direction * speed
	move_and_slide()
```

### Node references

- Prefer an exported typed reference when a designer should wire the dependency.
- Use `%StableName` only when the node is explicitly marked as scene-unique.
- Use a short `$Child/Path` for private, stable children owned by the same scene.
- Do not repeatedly search the whole tree in frame callbacks.
- Do not make a brittle relative path cross reusable-scene boundaries.

## Verification

Use the executable and commands already established by the project. When no project command exists, a detected Godot executable can perform a basic import and parse check with a command such as:

```sh
godot --headless --editor --path <project-root> --quit
```

Then verify all relevant behavior:

- The editor imports without parser, missing-resource, or invalid-node warnings.
- The affected scene runs with `F6`-equivalent behavior and does not rely accidentally on the main scene.
- The full project runs from its configured main scene.
- Every new Input Map action exists and each intended device binding works.
- Local and global transforms remain correct after instantiation and reparenting.
- Exported resources and node references are assigned in every scene instance.
- The Output and Debugger panels remain free of new errors.
- The Remote scene tree shows instances under the intended owner and they leave the tree when expected.
- Existing automated tests still pass.

Report the exact checks run and any editor-only checks that could not be automated.

## Failure Modes

- **Scene works only from the main project:** the reusable scene reaches outside its ownership boundary. Export the dependency or provide an explicit setup method.
- **`Node not found`:** a path, unique-name flag, or scene hierarchy changed. Inspect the actual `.tscn`; do not guess a replacement path.
- **Action appears inert:** the action is absent or misspelled in the Input Map, UI consumed the event, or the node's process mode is disabled or paused.
- **Instances change each other:** mutable state was stored in a shared resource. Move runtime state to the instance or duplicate the resource intentionally.
- **Wrong position after spawning:** local and global coordinates were mixed, or the transform was set before parenting.
- **Child access is null:** access happened before `_ready()`, the child is optional, or the script is attached to a different scene shape.
- **Physics differs by frame rate:** movement used `_process()` or applied `delta` inconsistently.
- **Editor shows stale assets:** source import settings were bypassed or generated cache files were edited.

## References

- [Nodes, scenes, and resources](references/nodes-scenes-resources.md)
- [Typed GDScript and input](references/typed-gdscript-input.md)
- [Editor and debugging workflow](references/editor-debugging.md)
