# Editor and Debugging Workflow

## Read the Project as Godot Reads It

The editor presents several related file types:

- `project.godot` stores project-level configuration, input actions, autoload registrations, and the main scene.
- `.tscn` stores a text scene: external resources, subresources, nodes, properties, groups, and editor-made connections.
- `.tres` stores a text resource independent of a scene.
- Source assets are imported into generated cache data under `.godot/`; edit the source or import options, not the cache.
- `.uid` files may provide stable resource identity in versions and projects that use them. Preserve the project's convention.

Before changing a serialized file manually, inspect a nearby editor-generated example. Property names and serialization details vary across Godot 4.x releases.

## Use the Editor Surfaces Deliberately

- **Scene:** confirm parentage, node type, ownership, warnings, unique-name flags, groups, and inherited-scene overrides.
- **FileSystem:** confirm canonical `res://` paths, imports, dependencies, and file moves.
- **Inspector:** distinguish a default value, a scene override, an external resource, and a built-in subresource.
- **Node:** inspect editor-created signal connections and groups.
- **Output:** catch parser errors, engine warnings, explicit logs, and failed assertions.
- **Debugger:** inspect errors, stack traces, breakpoints, and live variables.
- **Remote scene tree:** inspect the runtime tree rather than assuming it matches the local scene tab.
- **Profiler and Monitors:** establish evidence before optimizing frame, physics, memory, or object behavior.

## Establish a Reproducible Loop

1. Save all affected scenes and resources.
2. Reproduce the original behavior with the smallest reliable sequence.
3. Record whether the issue occurs when running the current scene, the main project, or both.
4. Make one coherent change.
5. Let Godot import and parse.
6. Repeat the same sequence.
7. Inspect the Remote tree and Debugger if visible behavior differs from the local scene.
8. Run the broader project and existing tests before finishing.

## Command-Line Checks

First discover the executable and repository convention. Common executable names differ by platform and installation. Do not hardcode one into project scripts without confirmation.

A basic editor import/parse pass is commonly run as:

```sh
godot --headless --editor --path <project-root> --quit
```

Run a project-defined test harness when present. A headless startup is not proof that visual layout, input, physics, audio, or scene transitions work.

## Debug Common Symptoms

### Parser or class resolution errors

- Fix the first error first; later errors may be cascading.
- Confirm `class_name` collisions do not exist.
- Confirm a referenced script parses before diagnosing its consumers.
- Check whether syntax belongs to a newer Godot 4.x release than the project.

### Missing node or resource

- Inspect the serialized scene and Remote tree.
- Confirm exact case in `res://` paths, especially for case-sensitive export targets.
- Confirm the node is owned by the packed scene and not only visible in an unsaved editor state.
- Confirm an exported slot is assigned on every relevant instance.
- Confirm a renamed or moved file retained the references expected by the project.

### Nothing processes

- Confirm the node entered the tree and is not disabled.
- Inspect `process_mode`, tree pause state, and visibility-dependent logic.
- Confirm the callback name and signature are exact.
- Confirm the running scene contains the edited script instance.

### Collision or overlap does not fire

- Use visible collision shapes while debugging.
- Check layer and mask in both directions.
- Confirm the shape is assigned and enabled.
- Confirm `Area2D.monitoring` or `monitorable` is appropriate.
- Confirm physics changes are not being made unsafely during a physics callback.

### Local scene differs from project run

- Compare the current scene's dependencies with the configured main scene.
- Look for assumptions about autoloads, parent paths, camera selection, project settings, or startup data.
- Make reusable scenes accept dependencies explicitly rather than reaching into a presumed parent.

## Completion Evidence

A useful final report names:

- Files changed.
- Godot version targeted.
- Automated commands run and their results.
- Manual scene and project flows exercised.
- Remaining checks that require the editor, a display, audio hardware, or a specific input device.
