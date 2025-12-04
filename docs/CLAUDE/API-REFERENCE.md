# {{PROJECT_NAME}} API Reference

**Base URL:** `{{API_BASE_URL}}`
**Version:** {{VERSION}}

**Related Documents:**
- [ARCHITECTURE.md](ARCHITECTURE.md) - System architecture
- [DEVELOPMENT.md](DEVELOPMENT.md) - Development guidelines

---

## Authentication

### Authentication Methods

| Method | Use Case | Header |
|--------|----------|--------|
| Bearer Token | Production | `Authorization: Bearer <token>` |
| API Key | Service-to-service | `X-API-Key: <key>` |

### Development Mode

<!-- Document any development-specific authentication bypass -->

When `{{DEV_MODE_SETTING}}` is enabled:
- All requests are automatically authenticated
- Test user has all permissions
- No token required

---

## Authorization

### Policies

| Policy | Description | Required Claims |
|--------|-------------|-----------------|
| | | |

---

## Common Response Codes

| Code | Meaning | When Returned |
|------|---------|---------------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST that creates resource |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Validation errors, malformed request |
| 401 | Unauthorized | Missing or invalid authentication |
| 403 | Forbidden | Authenticated but not authorized |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Resource state conflict |
| 500 | Internal Server Error | Unexpected server error |

---

## Error Response Format

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "Bad Request",
  "status": 400,
  "errors": {
    "fieldName": ["Error message"]
  },
  "traceId": "00-abc123-def456-00"
}
```

---

## Pagination

Paginated endpoints accept these query parameters:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | int | 1 | Page number (1-based) |
| `pageSize` | int | 20 | Items per page (max 100) |

Paginated responses include:

```json
{
  "items": [...],
  "page": 1,
  "pageSize": 20,
  "totalCount": 150,
  "totalPages": 8,
  "hasNextPage": true,
  "hasPreviousPage": false
}
```

---

## Endpoints

<!--
Document your API endpoints below.
Group by resource/controller.
Include request/response examples.
-->

### Resource 1

#### GET /api/v1/resources

Get all resources (paginated).

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `page` | int | No | Page number |
| `pageSize` | int | No | Items per page |
| `search` | string | No | Search filter |

**Response:** `200 OK`
```json
{
  "items": [
    {
      "id": "uuid",
      "name": "string",
      "createdDate": "2025-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pageSize": 20,
  "totalCount": 1
}
```

---

#### GET /api/v1/resources/{id}

Get a specific resource by ID.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | uuid | Resource ID |

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "name": "string",
  "description": "string",
  "createdDate": "2025-01-01T00:00:00Z",
  "modifiedDate": "2025-01-01T00:00:00Z"
}
```

**Errors:**
- `404 Not Found` - Resource doesn't exist

---

#### POST /api/v1/resources

Create a new resource.

**Request Body:**
```json
{
  "name": "string (required, max 200)",
  "description": "string (optional, max 2000)"
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "name": "string",
  "description": "string",
  "createdDate": "2025-01-01T00:00:00Z"
}
```

**Headers:**
- `Location: /api/v1/resources/{id}`

**Errors:**
- `400 Bad Request` - Validation errors

---

#### PUT /api/v1/resources/{id}

Update a resource.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | uuid | Resource ID |

**Request Body:**
```json
{
  "name": "string (required)",
  "description": "string (optional)"
}
```

**Response:** `200 OK`

**Errors:**
- `400 Bad Request` - Validation errors
- `404 Not Found` - Resource doesn't exist

---

#### DELETE /api/v1/resources/{id}

Delete a resource.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | uuid | Resource ID |

**Response:** `204 No Content`

**Errors:**
- `404 Not Found` - Resource doesn't exist
- `409 Conflict` - Resource cannot be deleted (has dependencies)

---

<!-- Add more endpoint groups as needed -->

### Resource 2

<!-- Copy the pattern above for additional resources -->

---

## DTOs Reference

### Common DTOs

#### ResourceListDto
```csharp
public class ResourceListDto
{
    public Guid Id { get; set; }
    public string Name { get; set; }
    public DateTime CreatedDate { get; set; }
}
```

#### ResourceDetailDto
```csharp
public class ResourceDetailDto
{
    public Guid Id { get; set; }
    public string Name { get; set; }
    public string? Description { get; set; }
    public DateTime CreatedDate { get; set; }
    public DateTime? ModifiedDate { get; set; }
}
```

#### CreateResourceRequest
```csharp
public class CreateResourceRequest
{
    [Required]
    [MaxLength(200)]
    public string Name { get; set; }

    [MaxLength(2000)]
    public string? Description { get; set; }
}
```

---

## Webhooks

<!-- If your API supports webhooks, document them here -->

| Event | Payload | Description |
|-------|---------|-------------|
| | | |

---

## Rate Limiting

| Scope | Limit | Window |
|-------|-------|--------|
| Global | 100 requests | 1 minute |
| Per endpoint | Varies | 1 minute |

**Response Headers:**
- `X-RateLimit-Limit`: Maximum requests allowed
- `X-RateLimit-Remaining`: Requests remaining in window
- `X-RateLimit-Reset`: Unix timestamp when limit resets

**Rate Limit Exceeded:** `429 Too Many Requests`

---

## Versioning

API versioning via URL path: `/api/v1/`, `/api/v2/`

| Version | Status | Notes |
|---------|--------|-------|
| v1 | Current | |

---

## Testing the API

### Using curl

```bash
# Get all resources
curl -X GET "{{API_BASE_URL}}/api/v1/resources" \
  -H "Authorization: Bearer <token>"

# Create a resource
curl -X POST "{{API_BASE_URL}}/api/v1/resources" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Resource"}'
```

### Swagger/OpenAPI

Interactive API documentation available at:
- Development: `https://localhost:{{PORT}}/swagger`
- Staging: `{{STAGING_URL}}/swagger`
