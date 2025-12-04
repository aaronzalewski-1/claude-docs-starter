# {{PROJECT_NAME}} Architecture

**Related Documents:**
- [CLAUDE.md](../../CLAUDE.md) - Overview and quick start
- [DEVELOPMENT.md](DEVELOPMENT.md) - Development guidelines
- [API-REFERENCE.md](API-REFERENCE.md) - API endpoints

---

## Technology Stack

| Component | Technology | Version | Notes |
|-----------|------------|---------|-------|
| Backend | {{TECH_STACK_BACKEND}} | | |
| Frontend | {{TECH_STACK_FRONTEND}} | | |
| Database | {{TECH_STACK_DATABASE}} | | |
| Cache | | | Optional |
| Message Queue | | | Optional |
| Cloud Provider | | | |

---

## Project Structure

```
{{PROJECT_NAME}}/
├── src/
│   ├── {{PROJECT_NAME}}.Domain/           # Domain entities, value objects
│   ├── {{PROJECT_NAME}}.Application/      # DTOs, interfaces, services
│   ├── {{PROJECT_NAME}}.Infrastructure/   # Data access, external services
│   └── {{PROJECT_NAME}}.API/              # Controllers, middleware
├── tests/
│   ├── {{PROJECT_NAME}}.UnitTests/
│   └── {{PROJECT_NAME}}.IntegrationTests/
└── docs/
    └── CLAUDE/
```

<!-- Customize the folder structure above to match your actual project -->

---

## Architecture Overview

### Clean Architecture Layers

```
┌─────────────────────────────────────────┐
│           Presentation Layer            │
│         (API Controllers, UI)           │
├─────────────────────────────────────────┤
│           Application Layer             │
│     (DTOs, Services, Interfaces)        │
├─────────────────────────────────────────┤
│           Infrastructure Layer          │
│   (Data Access, External Services)      │
├─────────────────────────────────────────┤
│             Domain Layer                │
│    (Entities, Value Objects, Logic)     │
└─────────────────────────────────────────┘
```

**Dependency Rule**: Dependencies point inward. Domain has no external dependencies.

---

## Database Schema

<!-- Document your database tables here -->

### Schema Overview

| Schema | Tables | Purpose |
|--------|--------|---------|
| dbo | | Default schema |
<!-- Add more schemas as needed -->

### Core Entities

#### Entity 1
<!-- Example entity documentation -->

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| Id | uniqueidentifier | PK | Primary key |
| Name | nvarchar(200) | NOT NULL | |
| CreatedDate | datetime2 | NOT NULL | |

**Relationships:**
- Has many [Related Entity]

---

## Domain Model

### Key Entities

<!-- List your main domain entities with brief descriptions -->

| Entity | Purpose | Key Behaviors |
|--------|---------|---------------|
| | | |

### Value Objects

<!-- List value objects used in your domain -->

| Value Object | Purpose | Validation Rules |
|--------------|---------|------------------|
| | | |

### Entity Relationships

```
┌─────────────┐       ┌─────────────┐
│   Entity1   │──────▶│   Entity2   │
└─────────────┘       └─────────────┘
       │
       ▼
┌─────────────┐
│   Entity3   │
└─────────────┘
```

<!-- Replace with your actual entity relationship diagram -->

---

## Configuration

### Application Settings Structure

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "{{CONNECTION_STRING}}"
  },
  "{{PROJECT_NAME}}Options": {
    // Project-specific configuration
  },
  "Authentication": {
    // Auth configuration
  },
  "Logging": {
    // Logging configuration
  }
}
```

### Environment Variables

| Variable | Purpose | Required |
|----------|---------|----------|
| | | |

---

## External Services

<!-- Document any external services or APIs your project integrates with -->

| Service | Purpose | Configuration |
|---------|---------|---------------|
| | | |

---

## Data Access Patterns

### Repository Pattern

<!-- If using repository pattern, document the approach -->

```csharp
// Example repository interface
public interface I{{Entity}}Repository
{
    Task<{{Entity}}?> GetByIdAsync(Guid id);
    Task<IEnumerable<{{Entity}}>> GetAllAsync();
    Task AddAsync({{Entity}} entity);
    Task UpdateAsync({{Entity}} entity);
    Task DeleteAsync(Guid id);
}
```

### Query Patterns

- Use `.AsNoTracking()` for read-only queries
- Use explicit `.Include()` for navigation properties
- Project to DTOs with `.Select()` for API responses

---

## Security

### Authentication

<!-- Document your authentication approach -->

| Mode | Description | When Used |
|------|-------------|-----------|
| Development | | Local development |
| Production | | Deployed environments |

### Authorization

<!-- Document authorization policies -->

| Policy | Required Claims/Roles | Endpoints |
|--------|----------------------|-----------|
| | | |

---

## Database Migrations

### Creating Migrations

```bash
# Add a new migration
{{MIGRATION_ADD_COMMAND}}

# Apply migrations
{{MIGRATION_APPLY_COMMAND}}

# List migrations
{{MIGRATION_LIST_COMMAND}}
```

### Migration Best Practices

1. Review generated migration code before applying
2. Test migrations on a copy of production data
3. Keep migrations small and focused
4. Include rollback considerations for breaking changes

---

## Performance Considerations

### Caching Strategy

<!-- Document your caching approach -->

| Cache Type | Use Case | TTL |
|------------|----------|-----|
| | | |

### Database Indexes

<!-- Document important indexes -->

| Table | Index | Columns | Purpose |
|-------|-------|---------|---------|
| | | | |

---

## Deployment

### Environments

| Environment | Purpose | URL |
|-------------|---------|-----|
| Development | Local development | localhost |
| Staging | Pre-production testing | |
| Production | Live environment | |

### Deployment Process

1. <!-- Step 1 -->
2. <!-- Step 2 -->
3. <!-- Step 3 -->

---

## Monitoring & Observability

### Health Checks

| Endpoint | Purpose |
|----------|---------|
| `/health` | Overall health status |
| `/health/ready` | Readiness probe (dependencies) |
| `/health/live` | Liveness probe (app running) |

### Logging

<!-- Document your logging approach and important log categories -->

| Category | Level | Purpose |
|----------|-------|---------|
| | | |

---

## Architectural Decisions

<!-- Document key architectural decisions and their rationale -->

### ADR 1: [Decision Title]

**Context:** [What is the situation?]

**Decision:** [What was decided?]

**Rationale:** [Why was this decided?]

**Consequences:** [What are the implications?]

---

<!-- Add more ADRs as needed -->
