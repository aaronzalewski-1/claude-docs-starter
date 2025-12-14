# {{PROJECT_NAME}} Core Library

<!--
  TEMPLATE FOR LIBRARY/SDK PROJECTS
  =================================
  Use this template when your project includes a reusable library or SDK component
  that is separate from your main application. Delete this file if not applicable.

  Examples:
  - A shared library used across multiple applications
  - A public SDK for external consumers
  - A "core" module with pure business logic (no infrastructure dependencies)
-->

**Related Documents:**
- [CLAUDE.md](../../CLAUDE.md) - Project overview
- [ARCHITECTURE.md](ARCHITECTURE.md) - System architecture
- [DEVELOPMENT.md](DEVELOPMENT.md) - Development guidelines

---

## Library Overview

<!-- Describe the library's purpose and scope -->

**Name:** `{{LibraryName}}`
**Purpose:** {{Brief description of what the library does}}
**Consumers:** {{Who uses this library - internal apps, external developers, etc.}}

### Design Principles

1. **{{Principle One}}** - {{Description}}
2. **{{Principle Two}}** - {{Description}}
3. **{{Principle Three}}** - {{Description}}

---

## Architecture Decision Records (ADRs)

<!--
  Document key architectural decisions for the library.
  Use this format for each ADR.
-->

### ADR-001: {{Decision Title}}

**Date:** {{YYYY-MM-DD}}
**Status:** Accepted | Superseded | Deprecated

**Context:**
{{What situation or problem prompted this decision?}}

**Decision:**
{{What was decided?}}

**Consequences:**
- {{Positive consequence}}
- {{Negative consequence or tradeoff}}

**Alternatives Considered:**
- {{Alternative 1}} - Rejected because {{reason}}
- {{Alternative 2}} - Rejected because {{reason}}

---

### ADR-002: {{Decision Title}}

<!-- Add more ADRs as needed -->

---

## Library vs. Application Separation

<!--
  Clearly define what belongs in the library vs. the application layer.
  This prevents scope creep and maintains clean boundaries.
-->

### Library Responsibilities (DO include)

| Category | Examples |
|----------|----------|
| Core logic | {{e.g., Validation rules, calculations, business algorithms}} |
| Pure models | {{e.g., Domain entities, value objects}} |
| Interfaces | {{e.g., Repository contracts, service interfaces}} |
| {{Category}} | {{Examples}} |

### Application Responsibilities (DO NOT include in library)

| Category | Examples |
|----------|----------|
| Infrastructure | {{e.g., Database access, HTTP clients, file I/O}} |
| Configuration | {{e.g., Connection strings, API keys, environment settings}} |
| UI concerns | {{e.g., View models, presentation logic}} |
| {{Category}} | {{Examples}} |

### Boundary Rules

1. **No external dependencies** - Library should have minimal NuGet/npm/pip packages
2. **No I/O operations** - No database, file, or network access
3. **No framework coupling** - Avoid tight coupling to ASP.NET, React, etc.
4. **Testable in isolation** - All logic testable without mocks for external services

---

## Public API Surface

<!--
  Document the public API that consumers interact with.
  This serves as a contract that shouldn't change without versioning.
-->

### Primary Entry Points

| Class/Function | Purpose | Stability |
|----------------|---------|-----------|
| `{{ClassName}}` | {{What it does}} | Stable / Beta / Experimental |
| `{{FunctionName}}` | {{What it does}} | Stable / Beta / Experimental |

### Extension Points

<!-- Document ways consumers can extend or customize library behavior -->

| Extension Point | How to Use |
|-----------------|------------|
| `{{InterfaceName}}` | Implement to provide custom {{behavior}} |
| `{{EventName}}` | Subscribe to handle {{event type}} |

### Breaking Change Policy

<!-- Define your approach to API changes -->

- **Major versions (X.0.0)**: May contain breaking changes
- **Minor versions (0.X.0)**: New features, backwards compatible
- **Patch versions (0.0.X)**: Bug fixes only

---

## Terminology

<!--
  Define domain-specific terms used in the library.
  Consistent terminology prevents confusion.
-->

| Term | Definition | Used In |
|------|------------|---------|
| {{Term}} | {{Definition}} | {{Where this term appears}} |
| {{Term}} | {{Definition}} | {{Where this term appears}} |

### Naming Conventions

<!-- Document any naming conventions specific to the library -->

| Context | Convention | Example |
|---------|------------|---------|
| {{Context}} | {{Convention}} | {{Example}} |

---

## Testing Guidelines

### Unit Test Patterns

<!-- Document how to test library code -->

```csharp
// Example test pattern for {{LibraryName}}
[Fact]
public void {{MethodName}}_{{Scenario}}_{{ExpectedResult}}()
{
    // Arrange
    var sut = new {{ClassName}}();

    // Act
    var result = sut.{{MethodName}}({{inputs}});

    // Assert
    result.Should().Be({{expected}});
}
```

### Test Data Conventions

<!-- Document any conventions for test data -->

| Data Type | Convention |
|-----------|------------|
| {{Type}} | {{How test data should be created}} |

---

## Version History

<!-- Track library versions separately from application versions if needed -->

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | {{Date}} | Initial release |

---

## Migration Guide

<!-- Document breaking changes and migration paths between versions -->

### Migrating from v{{X}} to v{{Y}}

**Breaking Changes:**
1. {{Change description}}
   - **Before:** {{old pattern}}
   - **After:** {{new pattern}}

**New Features:**
- {{Feature description}}

---

## Resources

- {{Link to API documentation}}
- {{Link to sample applications}}
- {{Link to contributing guidelines}}
