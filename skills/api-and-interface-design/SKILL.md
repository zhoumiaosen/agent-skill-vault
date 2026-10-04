---
name: api-and-interface-design
description: Use when defining or changing game module interfaces, Unity C# service boundaries, commands and events, asynchronous resource lifetimes, save contracts, backend service APIs or network protocols, especially when multiple callers depend on observable behavior.
license: MIT
---

# API and Interface Design

Design a small contract that callers can use without knowing the implementation. In a game, observable behavior includes state mutation, event order, object lifetime and save compatibility, not just method signatures.

## Inputs and scope

Inspect the requested use case, current consumers, module/assembly boundaries, engine and C# version, async conventions, serialization format, supported save versions and target platforms. Check existing tests before redesigning. Identify who owns state, which callers can mutate it, and whether there is actually a backend.

Scale the design to the change. Do not introduce a generic service framework, event bus, DI container, transport or repository layer solely to satisfy this skill. A draft contract does not authorize implementation, a breaking migration, data deletion or deployment.

## 1. Draw the boundary around responsibility

For Unity RPG systems, distinguish domain rules, application orchestration, presentation and persistence/engine adapters where the project benefits from that separation. A quest system should request an inventory operation rather than reach into a UI component's fields.

Keep portable domain contracts free of `GameObject`, `MonoBehaviour`, sprites and asset handles unless the contract intentionally belongs to an engine-facing layer. Preserve existing `.asmdef` dependencies and runtime/editor separation; use Unity's [assembly definition guidance](https://docs.unity3d.com/2022.3/Documentation/Manual/ScriptCompilationAssemblyDefinitionFiles.html) for the actual project version. A C# interface alone does not enforce an architectural boundary.

Specify typed identities where accidental interchange matters, units for numeric values, null/absence rules, bounds and mutability. Distinguish input commands, returned results, read-only snapshots and notifications. A read-only collection view is not necessarily an immutable snapshot; define whether values can change after return.

## 2. Define behavior before the implementation

For each public operation, record:

- Caller, state owner, required inputs and preconditions
- Success result, invariant-preserving state changes and commit point
- Expected rejection/error codes, unexpected failures, and whether any state changed
- Ordering, reentrancy/concurrency and main-thread requirements
- Async completion, cancellation, timeout and retry meaning
- Event publication and persistence guarantees

Choose error semantics appropriate to the layer. Gameplay rejection such as insufficient mana or full inventory should have a predictable typed outcome; unexpected infrastructure failures remain distinguishable. Do not map every failure to `false`, `null` or an empty catch. Match supported C# and project conventions rather than assuming the newest language features.

Validate external commands, save files, authoring data, network payloads and third-party responses at their boundaries. Retain internal invariant checks where mutable state, deserialization or concurrency can invalidate earlier assumptions. Static types do not prove that gameplay data is valid.

## 3. Make events and lifetimes explicit

State whether an event is a request or a fact that has already committed. Define publication thread, ordering/sequence, replay or duplicate behavior and subscriber-exception handling. Let consumers rebuild durable state from a snapshot when notifications are missed; do not make a transient UI event the sole record of a granted reward.

Name the owner of each subscription, async operation and loaded resource. Define subscribe/unsubscribe and acquire/release pairs for that owner's lifetime: application, scene, entity, pooled object or UI binding. Test disable/re-enable and scene unload. Static subscriptions also need a reset strategy for the project's [domain-reload settings](https://docs.unity3d.com/2022.3/Documentation/Manual/DomainReloading.html).

For asynchronous UI loads, define how a result is rejected when its target has been destroyed, recycled or rebound. Cancellation of the caller's wait does not establish cancellation of the underlying operation or rollback of a committed mutation. Specify who observes late completion/failure and releases resources safely under the package contract. Verify engine-object access and continuation threading for the actual async library.

For Addressables, verify the installed package's ownership and release behavior; [its memory-management guidance](https://docs.unity3d.com/Packages/com.unity.addressables@1.21/manual/MemoryManagement.html) explains why releasing ownership is not a guarantee that memory is immediately reclaimed. Do not infer correctness from a declining handle count alone.

## 4. Treat persistence as a versioned contract

Separate runtime object graphs and authoring assets from the save representation when their lifetimes or serialization rules differ. Use stable domain IDs, an explicit schema version and documented defaults. Preserve asset references and metadata when changing Unity-facing types. Check the selected serializer and [Unity serialization rules](https://docs.unity3d.com/2022.3/Documentation/Manual/script-Serialization.html); a public interface, property, dictionary or generic type is not automatically persistable by every serializer.

List supported old-save fixtures and migrations. Decide how to handle missing content, removed IDs, unknown fields, corrupt data and newer unsupported schemas. If an older save lacks claim receipts, define how existing progress establishes prior rewards; missing receipts must not automatically regrant them. Unresolvable legacy history needs an explicit migration-policy decision, not an in-flight/pending outcome that encourages waiting or retrying. Preserve the original save on failure; do not silently reset progress. Adding an optional field can still alter defaults, interpretation or serialized layout, so test compatibility rather than calling every addition safe.

When one operation changes several persisted facts, define one transaction/snapshot or a recoverable journal using the existing persistence layer. Validate the actual target platform's write, replacement and durability behavior; a sequence of ordinary writes is not an atomic commit.

### Example: offline quest-reward contract

The application reward service owns inventory mutation and claim receipts. `ClaimReward` receives a stable save/character identity, quest-completion identity and reward version; validate eligibility and derive or validate the authoritative payload from quest data. One completion keeps one claim identity across retries; repeatable completions get distinct identities.

The same identity and payload returns the recorded outcome; a changed payload is rejected. Serialize concurrent claims through the authoritative state owner. Commit the inventory change and claim receipt together, or reconcile a durable journal after interruption. Define pending/unknown outcomes explicitly; do not retry an uncertain side effect blindly. Retain deduplication evidence for as long as that save can replay the intent.

UI cancellation cannot revoke a committed reward. Publish notifications after the defined commit point, allow snapshot reconstruction after missed events, and keep failed icon loading independent from the grant. This is a design example, not implemented or runtime-tested code.

## 5. Add networking only when the feature needs it

For a real backend or multiplayer boundary, define authority and authorization, protocol/version compatibility, payload validation, timeouts, ordering and retries. Choose transport-specific conventions deliberately; HTTP status codes and pagination are not defaults for in-process C# calls.

For retryable state changes, scope the stable intent key to its owner and operation, validate reused payloads and claim ownership atomically. Persist the outcome and reconcile uncertain results. A unique key alone cannot guarantee an external side effect is atomic with local storage. Use the provider's idempotency support or an explicit recovery design. Retention must cover all permitted retry/replay paths; do not claim exactly-once behavior from a queue setting alone.

In Godot or Unreal, map the same contract questions to nodes/signals/resources or actors/delegates/UObjects and the project's save system. Verify their lifetime and reflection rules rather than copying Unity APIs.

## 6. Verify consumers and failure paths

Test the relevant contract before declaring it ready:

- Normal operation, invalid input and rejection without partial mutation
- Sequential/concurrent duplicate requests and different-payload collisions
- Reentrant subscribers, missed/repeated notifications and snapshot recovery
- Unload/destruction, pooling, disable/re-enable and late async completion
- Crash or interrupted persistence around the commit point; old-save migration and corruption handling
- Actual target compile/player behavior for serializer, reflection/AOT and engine-lifetime assumptions

For changes to an existing public contract, inspect callers and serialized data. Explain observable changes and provide a scoped migration/adaptor plan where needed; do not impose multiple versions or forbid them universally. Keep compatibility fixtures until the project explicitly retires support.

## Deliverable and stopping conditions

Return the contract, ownership/dependency map, important decisions, compatibility/migration plan and test evidence. Separate verified behavior from proposals and tests not run. If ownership, durability or a breaking behavior is unresolved, pause the dependent implementation and ask the smallest consequential question. With no engine or persistence environment available, deliver a reviewable design, not a runtime-readiness claim.

Attribution and adaptation history: [SOURCE.md](SOURCE.md). License: [LICENSE](LICENSE).
