# Nodes, Scenes, and Resources

## Select the Runtime Shape

Start with the behavior the engine must provide:

- Use `Node` for non-spatial behavior whose lifetime belongs to a scene.
- Use `Node2D` or `Node3D` when children need a shared transform.
- Use `Control` when anchors, offsets, containers, focus, or mouse filtering should drive layout and interaction.
- Use `Area2D` or `Area3D` for overlap detection without solid collision response.
- Use `CharacterBody2D` or `CharacterBody3D` for script-directed collision movement.
- Use `RigidBody2D` or `RigidBody3D` when the physics solver should own motion.
- Use `StaticBody2D` or `StaticBody3D` for collision geometry that does not move during simulation.

Do not select a root solely because it renders the object. A reusable actor can have a behavioral root with sprite, collider, audio, and marker children.

## Draw Scene Boundaries

A branch deserves its own scene when at least one condition holds:

- It appears in more than one parent scene.
- It has a meaningful independent lifecycle, such as an enemy, dialog, projectile, or room.
- It needs isolated editing or testing.
- Its child structure is an implementation detail that parents should not manipulate.
- A designer should configure instances through exported properties.

Keep the root's public contract small. A parent should call an actor's methods or set exported configuration, not reach through several children to make it work.

## Respect Ownership and Transforms

The parent that creates a node normally owns its lifetime. Keep dynamically created nodes under a dedicated container in that parent's scene:

```text
Arena
|-- Actors
|-- Effects
`-- Interface
```

Transforms are parent-relative:

- `position`, `rotation`, and `scale` are local for `Node2D`.
- `transform` is local and `global_transform` is world-relative.
- `Control` layout uses anchors and offsets; treating it like `Node2D` usually produces fragile UI.
- Reparenting can change the visible transform unless the operation preserves the global transform.

When spawning, add the node to its intended parent and then set its global position:

```gdscript
func add_effect(effect_scene: PackedScene, world_position: Vector2) -> void:
	var effect := effect_scene.instantiate() as Node2D
	if effect == null:
		return
	%Effects.add_child(effect)
	effect.global_position = world_position
```

## Treat PackedScene as a Factory

A `.tscn` file is loaded as a `PackedScene`; each `instantiate()` call creates a new node branch. The returned root type is not guaranteed by the `PackedScene` property, so validate a cast when code requires a specific API.

Prefer an exported scene when designers choose the implementation:

```gdscript
@export var actor_scene: PackedScene
```

Prefer `preload()` when the dependency is fixed and local to the script:

```gdscript
const SPARK_SCENE: PackedScene = preload("res://effects/spark.tscn")
```

Do not use an arbitrary string path when a typed Inspector slot can represent the same relationship.

## Separate Definition Data from Instance State

Custom resources are effective definition assets:

```gdscript
class_name CollectibleSpec
extends Resource

@export var id: StringName
@export_range(1, 999, 1) var points: int = 1
@export var icon: Texture2D
```

A scene can consume the definition while keeping runtime state on its node:

```gdscript
class_name Collectible
extends Area2D

@export var spec: CollectibleSpec
var collected: bool = false

func point_value() -> int:
	return spec.points if spec != null else 0
```

The resource describes a kind of collectible. The node tracks whether this particular instance was collected. If code changes `spec.points`, every consumer sharing that resource sees the change.

Use these rules:

- External resource: shared definition or asset with its own identity.
- Built-in subresource: configuration private to one owning file.
- `resource_local_to_scene`: only when each scene instance truly needs its own resource copy and the exact project version supports the intended behavior.
- `duplicate(true)`: an explicit deep copy when runtime mutation is required; verify nested resources because copy behavior matters.

## Use Stable References

Reference choices, from most explicit to most structural:

1. A typed `@export` property for cross-branch dependencies configured in the editor.
2. A setup method parameter for runtime-created dependencies.
3. A scene-unique `%Name` for an intentionally stable descendant.
4. A short `$Child` path for a private child owned by the same scene.
5. A group lookup for discovery of a category, not for finding one assumed singleton.

Avoid paths that climb out of a reusable scene. They make the child silently depend on whichever parent happens to instantiate it.

## Lifecycle Checklist

- `_init()` runs before the node is in the tree; scene children are not ready.
- `_enter_tree()` runs when the node joins the tree.
- Child `_ready()` callbacks run before their parent's `_ready()`.
- `@onready` expressions resolve immediately before that script's `_ready()`.
- `_exit_tree()` is the final place to release non-tree resources or unregister from external systems.
- `queue_free()` schedules safe removal; code later in the frame must still avoid treating the node as durable.

For a reusable scene, test both direct execution and instantiation under its normal parent. These exercises reveal different dependency mistakes.
