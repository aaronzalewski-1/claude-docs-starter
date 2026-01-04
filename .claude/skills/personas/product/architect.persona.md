---
name: architect-knowledge
description: Domain expertise for Architect persona - SOLID principles, pattern catalog, coupling metrics, and architectural evaluation
type: persona_skill
persona: personas/product/architect
version: 1.0.0
---

# Architect Domain Knowledge

> Structural principles, patterns, and metrics for evaluating architectural decisions.

---

## SOLID Principles

### Single Responsibility Principle (SRP)

**Definition**: A class should have only one reason to change.

| Good | Bad |
|------|-----|
| `OrderValidator` - validates orders | `OrderManager` - validates, saves, emails, logs |
| `EmailSender` - sends emails | `UserService` - CRUD + auth + notifications |

**Detection Questions:**
- Does this class have multiple "actors" (stakeholders who might request changes)?
- If I describe the class, do I use "and" multiple times?
- Would changes to feature A require touching code for feature B?

**Refactoring Pattern:**
```
OrderManager (violates SRP)
    ↓ Extract
OrderValidator + OrderRepository + OrderNotifier + OrderLogger
```

---

### Open/Closed Principle (OCP)

**Definition**: Open for extension, closed for modification.

| Good | Bad |
|------|-----|
| Strategy pattern for payment methods | Switch statement with payment type cases |
| Decorator for logging variations | Adding `if (logLevel == ...)` everywhere |

**Detection Questions:**
- To add a new variant, do I modify existing code or add new code?
- Are there switch/if-else chains on type discriminators?
- Can I add behavior without touching the core class?

**Refactoring Pattern:**
```
// Before: Closed for extension
function calculateDiscount(customer) {
    if (customer.type === "Gold") return 0.2;
    if (customer.type === "Silver") return 0.1;
    return 0;
}

// After: Open for extension
interface DiscountStrategy { calculate(customer): number; }
class GoldDiscount implements DiscountStrategy { ... }
class SilverDiscount implements DiscountStrategy { ... }
```

---

### Liskov Substitution Principle (LSP)

**Definition**: Subtypes must be substitutable for their base types without altering correctness.

| Good | Bad |
|------|-----|
| `Square` and `Rectangle` as separate types | `Square extends Rectangle` (breaks SetWidth/SetHeight contract) |
| `ReadOnlyList<T>` vs `List<T>` | `ReadOnlyList extends List` (Add() throws) |

**Detection Questions:**
- Does the subtype throw exceptions for inherited methods?
- Does the subtype ignore or weaken preconditions?
- Would tests for the base type fail on the subtype?

**Violation Indicators:**
- `throw new NotImplementedException()`
- `throw new InvalidOperationException()` in overridden methods
- Overridden methods that do nothing

---

### Interface Segregation Principle (ISP)

**Definition**: Clients should not be forced to depend on methods they don't use.

| Good | Bad |
|------|-----|
| `IReadable`, `IWritable`, `IDeletable` | `IRepository<T>` with 20 methods |
| `INotifier` (just Send) | `IUserService` (CRUD + Auth + Profile + Settings) |

**Detection Questions:**
- Do implementers have empty methods or throw NotImplementedException?
- Does the interface have more than 5-7 methods?
- Do some clients only use a subset of methods?

**Refactoring Pattern:**
```
// Before: Fat interface
interface Repository<T> {
    get(id): T;
    getAll(): T[];
    add(entity: T): void;
    update(entity: T): void;
    delete(id): void;
    bulkInsert(entities: T[]): void;
    executeRawSql(sql: string): void;
    // ... 10 more methods
}

// After: Segregated
interface ReadRepository<T> { get(id): T; getAll(): T[]; }
interface WriteRepository<T> { add(entity: T): void; update(entity: T): void; }
interface DeleteRepository<T> { delete(id): void; }
```

---

### Dependency Inversion Principle (DIP)

**Definition**: High-level modules should not depend on low-level modules. Both should depend on abstractions.

| Good | Bad |
|------|-----|
| `OrderService(IOrderRepository repo)` | `OrderService { new SqlOrderRepository() }` |
| Constructor injection | Static factory calls |

**Detection Questions:**
- Does this class instantiate its dependencies with `new`?
- Would I need to modify this class to change a dependency?
- Can I unit test this class without a database/network?

**Dependency Direction:**
```
✓ Good: Domain → Application → Infrastructure
         (Abstractions flow inward)

✗ Bad:   Domain ← Application ← Infrastructure
         (Concrete types leak outward)
```

---

## Pattern Catalog

### Creational Patterns

| Pattern | Use When | Example |
|---------|----------|---------|
| **Factory Method** | Need to delegate instantiation to subclasses | `LoggerFactory.createLogger()` |
| **Abstract Factory** | Families of related objects | `DbProviderFactory` (connections, commands) |
| **Builder** | Complex object construction with many options | `StringBuilder`, `QueryBuilder` |
| **Singleton** | Exactly one instance needed (use sparingly!) | Config (via DI, not static) |

### Structural Patterns

| Pattern | Use When | Example |
|---------|----------|---------|
| **Adapter** | Convert interface to match expected interface | Wrapping legacy API |
| **Decorator** | Add behavior without modifying class | `BufferedStream(FileStream)` |
| **Facade** | Simplify complex subsystem | `HttpClient` (hides sockets, SSL) |
| **Proxy** | Control access or add cross-cutting concerns | Lazy loading, caching |

### Behavioral Patterns

| Pattern | Use When | Example |
|---------|----------|---------|
| **Strategy** | Interchangeable algorithms | Comparators, payment processors |
| **Command** | Encapsulate requests as objects | Undo/redo, CQRS |
| **Observer** | One-to-many notifications | Events, Pub/Sub |
| **Template Method** | Define algorithm skeleton, let subclasses fill steps | Framework lifecycle hooks |

---

## Coupling Metrics

### Afferent Coupling (Ca) - Incoming

**Definition**: Number of types that depend on this type.

| Ca Value | Interpretation | Risk |
|----------|---------------|------|
| 0 | Unused code? | Consider removal |
| 1-5 | Healthy | Low change impact |
| 6-15 | Central component | Test thoroughly |
| >15 | Hub | Changes are risky |

### Efferent Coupling (Ce) - Outgoing

**Definition**: Number of types this type depends on.

| Ce Value | Interpretation | Risk |
|----------|---------------|------|
| 0-3 | Well-focused | Easy to test |
| 4-8 | Typical service | Normal |
| 9-15 | Orchestrator | May need decomposition |
| >15 | God class | Refactor urgently |

### Instability (I)

**Formula**: `I = Ce / (Ca + Ce)`

| I Value | Interpretation |
|---------|---------------|
| 0 | Maximally stable (many dependents, few dependencies) |
| 1 | Maximally unstable (few dependents, many dependencies) |

**Stable Dependency Principle**: Depend in the direction of stability.
- Stable components (I→0) should be depended upon
- Unstable components (I→1) can depend on stable ones

---

## Clean Architecture Layers

```
┌─────────────────────────────────────────────┐
│              Presentation                    │  ← UI, Controllers, ViewModels
├─────────────────────────────────────────────┤
│             Application                      │  ← Service interfaces, DTOs, Use Cases
├─────────────────────────────────────────────┤
│            Infrastructure                    │  ← Database, External APIs, I/O
├─────────────────────────────────────────────┤
│               Domain                         │  ← Entities, Value Objects, Business Rules
└─────────────────────────────────────────────┘
```

### Layer Rules

| Rule | Violation Example |
|------|-------------------|
| Domain has no dependencies | ORM annotations in entity |
| Application defines interfaces | Concrete repository referenced |
| Infrastructure implements interfaces | Interface defined in Infrastructure |
| Presentation only references Application | Direct Infrastructure usage |

### Dependency Flow

```
✓ Allowed: Presentation → Application → Domain
✓ Allowed: Infrastructure → Application → Domain
✗ Forbidden: Domain → Infrastructure
✗ Forbidden: Application → Presentation
```

---

## Code Smell Detection

### Class-Level Smells

| Smell | Indicators | Remedy |
|-------|------------|--------|
| **God Class** | >500 lines, >10 dependencies, does "everything" | Extract classes by responsibility |
| **Data Class** | Only properties, no behavior | Add behavior or convert to record/struct |
| **Feature Envy** | Method uses another class's data more than its own | Move method to that class |
| **Inappropriate Intimacy** | Classes access each other's private members | Introduce interfaces, reduce coupling |

### Method-Level Smells

| Smell | Indicators | Remedy |
|-------|------------|--------|
| **Long Method** | >20 lines, multiple abstraction levels | Extract methods |
| **Long Parameter List** | >4 parameters | Introduce parameter object |
| **Flag Arguments** | `bool isVerbose`, `bool includeDeleted` | Split into separate methods |
| **Switch Statements** | Type-based switching | Replace with polymorphism |

### Architecture Smells

| Smell | Indicators | Remedy |
|-------|------------|--------|
| **Cyclic Dependencies** | A→B→C→A | Break cycle with interfaces |
| **Hub Dependency** | Everything depends on one class | Extract interfaces, reduce surface |
| **Scattered Changes** | One feature touches many files | Consolidate feature code |
| **Shotgun Surgery** | One change requires many edits | Extract shared abstraction |

---

## Evaluation Criteria

### Decision Quality Checklist

When evaluating an architectural decision:

- [ ] **SRP**: Does each class have a single responsibility?
- [ ] **OCP**: Can behavior be extended without modification?
- [ ] **LSP**: Are all subtypes substitutable?
- [ ] **ISP**: Are interfaces focused and cohesive?
- [ ] **DIP**: Do dependencies point toward abstractions?
- [ ] **Layer boundaries**: Are dependencies flowing correctly?
- [ ] **Testability**: Can components be tested in isolation?
- [ ] **Coupling**: Is Ce (efferent coupling) reasonable?

### Confidence Calibration

| Evidence Quality | Confidence Modifier |
|------------------|---------------------|
| Follows established codebase patterns | +0.1 |
| Aligns with SOLID principles | +0.1 |
| Maintains low coupling | +0.05 |
| Introduces new pattern (justified) | 0 |
| Violates SOLID (acknowledged tradeoff) | -0.1 |
| Creates cyclic dependency | -0.2 |
| Increases coupling significantly | -0.15 |
