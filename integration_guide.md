# Guía de Integración con core_aws

## Opción 1: Cliente Python (Recomendado)

### Instalación en core_aws
```bash
# Desde el directorio logs_aws
pip install -e .

# O copiar logs_client/ a core_aws/
```

### Uso en core_aws
```python
from logs_client import InteractionLogger

# En chat.py
logger_service = InteractionLogger("http://logs-service:8000")

# Logs de eventos
logger_service.log_event("query_start", session_id, 
                        question=request.question, profile=request.profile)
```

## Opción 2: HTTP Directo

### Endpoint /events
```bash
POST http://localhost:8000/events?event_type=query_start&session_id=123
Content-Type: application/json

{
  "question": "¿Cómo usar S3?",
  "profile": "developer"
}
```

### Endpoint /logs (genérico)
```bash
POST http://localhost:8000/logs
Content-Type: application/json

{
  "level": "INFO",
  "service": "core_aws", 
  "message": "query_start: session_123",
  "metadata": {
    "event_type": "query_start",
    "session_id": "session_123",
    "question": "¿Cómo usar S3?"
  }
}
```

## Configuración

### En core_aws .env
```
LOGS_SERVICE_URL=http://logs-service:8000
```

### Docker Compose (core_aws)
```yaml
services:
  core-aws:
    environment:
      - LOGS_SERVICE_URL=http://logs-service:8000
    depends_on:
      - logs-service
```