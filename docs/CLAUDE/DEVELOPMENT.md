# {{PROJECT_NAME}} Development Guidelines

**READ THIS FIRST** - Contains critical operational patterns, coding guidelines, and lessons learned.

**Related Documents:**
- [CLAUDE.md](../../CLAUDE.md) - Overview and quick start
- [ARCHITECTURE.md](ARCHITECTURE.md) - System architecture
- [CHANGELOG.md](CHANGELOG.md) - Version history

---

## Claude Operational Best Practices

**Purpose**: These are common mistakes that reduce Claude's velocity when working on codebases. Following these practices prevents repeated errors and improves efficiency.

### Windows/PowerShell Environment Awareness

<!-- Remove this section if not on Windows -->

| Mistake | Why It Fails | Correct Approach |
|---------|--------------|------------------|
| Using `Select-String` in bash | PowerShell cmdlet, not bash | Use `powershell -Command "... \| Select-String ..."` or use grep equivalent |
| Using `grep` directly in Windows cmd | grep is Unix, not Windows native | Wrap in `powershell -Command` or use `findstr` |
| Using forward slashes in `findstr` | Windows uses backslashes in paths | Use `\\` or switch to PowerShell `Select-String` |
| Mixing shell syntaxes | Bash and PowerShell have different syntax | Pick one shell and stay consistent within a command |

**Recommended Pattern for Windows:**
```bash
# Option 1: Use PowerShell explicitly
powershell -Command "dotnet build 2>&1 | Select-String -Pattern 'error|warning'"

# Option 2: Use cross-platform tools when available
dotnet build 2>&1  # Then parse output in response
```

### Tool Prerequisites

| Mistake | Prevention |
|---------|------------|
| "Edit failed. I need to read the file first." | **Always read a file before editing it.** The Edit tool requires prior Read. |
| Editing with stale context | If a file was read many messages ago, re-read it before editing. |
| Assuming file content from memory | After complex conversations, file state may have changed. When in doubt, re-read. |

### Build and Test Commands

| Mistake | Why It Fails | Correct Approach |
|---------|--------------|------------------|
| `--no-build` after code changes | Runs old compiled code, not your changes | Build explicitly or omit `--no-build` flag |
| Building when debugger has file locks | "The file is locked by another process" | Build a different project, or stop debugger first |
| Assuming build success without checking | May have silent warnings or errors | Always check build output before proceeding |

### External API Integration Guidelines

When working with external APIs (Azure services, third-party APIs, etc.):

| Mistake | Why It Fails | Correct Approach |
|---------|--------------|------------------|
| Assuming API behavior without checking | Claims about operations without verification | **Always read the API client implementation first** |
| Guessing endpoint paths | 404 errors, wrong API versions | Search for existing API client files |
| Making claims about data loss risks | User may trust incorrect information | Explicitly verify documentation for destructive operations |

**Recommended Pattern for External APIs:**
1. Find API client implementations in your codebase
2. Read the implementation - check base URLs, endpoint patterns, HTTP methods
3. If proposing new operations, verify vendor documentation
4. Acknowledge uncertainty: "I should verify the API docs for..."
5. Propose safe verification: GET requests first, then write operations

### General Velocity Principles

1. **Check environment first**: Consider shell context before running commands
2. **Read before edit**: Always read files before attempting to edit them
3. **Build after changes**: Don't use `--no-build` when testing modified code
4. **One shell per command**: Don't mix bash and PowerShell syntax
5. **Handle file locks gracefully**: If build fails due to locks, build individual projects or inform user

---

## Architectural Analysis Checklist

**Critical**: Follow these steps before making architectural recommendations.

| Step | Action | Why |
|------|--------|-----|
| 1 | **Read project documentation first** | Contains deployment model, design decisions, guiding principles |
| 2 | **Understand deployment model** | Single-tenant ≠ Multi-tenant. Ask clarifying questions. |
| 3 | **Question apparent "problems"** | Missing FKs or string IDs may be intentional design choices |
| 4 | **Validate against principles** | Check "Avoid Over-Engineering" principle |
| 5 | **If user challenges analysis** | Re-examine assumptions. Don't defend incorrect analysis. |

---

## Debugging Checklist

**Critical**: Follow this order when integration tests fail.

| Step | Action | Why |
|------|--------|-----|
| 1 | **Check infrastructure compatibility** | Verify target frameworks match. Version mismatches masquerade as bugs. |
| 2 | **Check authentication mode** | Dev mode may auto-authenticate. Don't debug auth that's bypassed. |
| 3 | **Get the actual error message** | Don't debug from HTTP status codes alone. Add logging to expose real exception. |
| 4 | **Verify test infrastructure** | Create minimal tests that verify ONE thing (database, schema, etc.) |
| 5 | **Add strategic logging** | Log at layer boundaries: Repository → Service → Controller |
| 6 | **Test layers independently** | Verify bottom-up: Database → Repository → Service → API |
| 7 | **Create minimal reproductions** | Simpler tests that verify one assumption at a time |
| 8 | **Trust diagnostic data** | If logs show data loading correctly, problem is NOT data loading |

**Key Insights:**
- **Get the actual error message first**: A 500 error could be a service bug, database constraint, or config issue - only the exception reveals which
- **Version compatibility matters**: Check target frameworks FIRST when tests fail after upgrades
- **Layer-by-layer verification is efficient**: Proves where the problem IS and ISN'T quickly

---

## Architectural Principles

### 1. Rich Domain Models
- Entities should have behavioral methods, not just properties
- Encapsulate business logic within domain entities
- Example: `order.Complete()` instead of manually setting `order.Status = "Completed"`

```csharp
// Good - Rich domain model
public class Order
{
    public void Complete()
    {
        if (Status != OrderStatus.Pending)
            throw new InvalidOperationException("Only pending orders can be completed");
        Status = OrderStatus.Completed;
        CompletedDate = DateTime.UtcNow;
    }
}

// Avoid - Anemic model
public class Order
{
    public OrderStatus Status { get; set; }
    public DateTime? CompletedDate { get; set; }
}
```

### 2. Proper Separation of Concerns
- **Controllers**: Route requests, validate input, return responses (thin layer)
- **Services**: Orchestrate operations, coordinate business workflows
- **Domain**: Business rules, invariants, and core logic
- **DTOs**: API boundaries only (never pass entities to/from API)

### 3. Dependency Management
- Use interfaces for all service dependencies
- Application layer defines interfaces, Infrastructure implements them
- Dependency Injection for all service registration
- **SOLID Principles**: Focus on Interface Segregation and Dependency Inversion

### 4. Avoid Over-Engineering
- Only add complexity when explicitly required
- Don't create abstractions for single-use code
- Don't add error handling for impossible scenarios
- Keep solutions minimal and focused on current requirements
- **Three similar lines of code > premature abstraction**
- Don't add features beyond what's requested
- Delete unused code completely

### 5. Testing Strategy
- **Unit tests**: Test domain logic and service methods with mocks
- **Integration tests**: Test API endpoints end-to-end
- Always align test DTOs with actual DTO properties
- Each test should be independent and repeatable

### 6. Code Cleanliness
- Delete unused code completely (no backwards-compatibility hacks)
- Use domain methods instead of primitive property operations
- Meaningful names that reveal intent
- No premature optimization or generalization
- Prefer editing existing files over creating new ones

---

## Code Organization Principles

### Clean Architecture Layers
- Domain entities have no external dependencies
- Application layer defines interfaces
- Infrastructure implements interfaces
- Presentation depends on application abstractions

### DTO Patterns
- Separate DTOs for List, Detail, Create, Update operations
- DTOs never expose internal IDs unnecessarily
- Include audit fields where relevant

### Service Layer Patterns
- Services accept and return DTOs, not entities
- Transaction management in service methods
- Validation before database operations
- Detailed exception messages for debugging

### API Controller Guidelines
- Use standard HTTP status codes (200, 201, 204, 400, 404, 500)
- Return DTOs, never entities
- Log errors with context
- Use CreatedAtAction for POST endpoints

---

## Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Entities | Singular nouns | `Order`, `Customer` |
| Collections | Plural property names | `Orders`, `Customers` |
| DTOs | Descriptive suffixes | `OrderListDto`, `OrderDetailDto` |
| Services | Interface + Implementation | `IOrderService`, `OrderService` |
| Controllers | Plural resource names | `OrdersController` |

---

## Lessons Learned from Real Refactorings

**Purpose**: Document mistakes made during development to prevent similar errors in the future.

<!--
Add your own case studies here as you encounter issues.
This section becomes more valuable over time as you capture real lessons.
-->

### Case Study Template

Use this format to document lessons learned:

---

**Case Study N: [Title] ([Date])**

**Context:** [What were you trying to do?]

**The Mistake:**
- [What went wrong? Be specific.]

**Why It Was Wrong:**
- [Root cause analysis]

**What Should Have Been Done:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Impact:**
- [Time wasted, bugs introduced, etc.]

**General Principles Derived:**
1. [Lesson 1]
2. [Lesson 2]

---

### Example Case Studies

<!-- These are placeholder examples. Replace with your own real experiences. -->

**Case Study 1: [Your First Lesson] ([Date])**

**Context:** [Describe the situation]

**The Mistake:** [What went wrong]

**Why It Was Wrong:** [Analysis]

**What Should Have Been Done:** [Correct approach]

**General Principles Derived:**
1. [Key takeaway]

---

## What to Avoid

- ❌ Anemic domain models (entities as mere data bags)
- ❌ Direct database access in controllers
- ❌ Manual DTO mapping in services (use AutoMapper or similar)
- ❌ Creating files unless absolutely necessary
- ❌ Premature optimization or generalization
- ❌ Adding features beyond what's requested
- ❌ Backwards-compatibility hacks for unused code

---

## File Operations Guidelines

- **ALWAYS prefer editing existing files** over creating new ones
- Read files before editing them (required by Edit tool)
- Use Edit tool for modifications, not bash commands
- Never create markdown/documentation files unless explicitly requested

---

## Session State Management

For complex or multi-session work:
1. Review recent git commits: `git log --oneline -10`
2. Check for in-progress work in `docs/CLAUDE/SESSION-STATE.json` if it exists
3. Run build to verify baseline
4. Load context-specific documentation based on task type
