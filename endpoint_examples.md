# Ejemplos de Consumo - Endpoint POST /logs

## 1. Ejemplo Básico
```bash
curl -X POST http://localhost:8000/logs \
  -H "Content-Type: application/json" \
  -d '{
    "level": "INFO",
    "service": "core_aws",
    "message": "Usuario realizó consulta",
    "metadata": {
      "session_id": "sess_123",
      "user_id": "user_456"
    }
  }'
```

## 2. Eventos de core_aws
```bash
# Query Start
curl -X POST http://localhost:8000/logs \
  -H "Content-Type: application/json" \
  -d '{
    "level": "INFO",
    "service": "core_aws",
    "message": "query_start: sess_123",
    "metadata": {
      "event_type": "query_start",
      "session_id": "sess_123",
      "question": "¿Cómo configurar S3?",
      "profile": "developer"
    }
  }'

# Model Attempt
curl -X POST http://localhost:8000/logs \
  -H "Content-Type: application/json" \
  -d '{
    "level": "DEBUG",
    "service": "core_aws", 
    "message": "model_attempt: sess_123",
    "metadata": {
      "event_type": "model_attempt",
      "session_id": "sess_123",
      "model": "gpt-4"
    }
  }'

# Response Generated
curl -X POST http://localhost:8000/logs \
  -H "Content-Type: application/json" \
  -d '{
    "level": "INFO",
    "service": "core_aws",
    "message": "response_generated: sess_123", 
    "metadata": {
      "event_type": "response_generated",
      "session_id": "sess_123",
      "model_used": "gpt-4",
      "tokens": 150,
      "response_time_ms": 2500
    }
  }'
```

## 3. Otros Microservicios
```bash
# Auth Service
curl -X POST http://localhost:8000/logs \
  -H "Content-Type: application/json" \
  -d '{
    "level": "INFO",
    "service": "auth_service",
    "message": "Usuario autenticado exitosamente",
    "metadata": {
      "user_id": "user_789",
      "method": "jwt",
      "ip": "192.168.1.100"
    }
  }'

# Payment Service
curl -X POST http://localhost:8000/logs \
  -H "Content-Type: application/json" \
  -d '{
    "level": "ERROR",
    "service": "payment_service",
    "message": "Error procesando pago",
    "metadata": {
      "order_id": "ord_456",
      "amount": 99.99,
      "error_code": "CARD_DECLINED"
    }
  }'
```

## 4. Python Requests
```python
import requests

# Ejemplo básico
payload = {
    "level": "INFO",
    "service": "core_aws",
    "message": "query_start: sess_123",
    "metadata": {
        "event_type": "query_start",
        "session_id": "sess_123",
        "question": "¿Cómo usar Lambda?",
        "profile": "developer"
    }
}

response = requests.post(
    "http://localhost:8000/logs",
    json=payload,
    timeout=5
)

print(response.json())
# {"status": "success", "message": "Log enviado a cola"}
```

## 5. JavaScript/Node.js
```javascript
const axios = require('axios');

const logData = {
    level: "INFO",
    service: "frontend_app",
    message: "Usuario navegó a dashboard",
    metadata: {
        user_id: "user_123",
        page: "/dashboard",
        timestamp: new Date().toISOString()
    }
};

axios.post('http://localhost:8000/logs', logData)
    .then(response => console.log(response.data))
    .catch(error => console.error('Error:', error));
```

## 6. Formato de Respuesta
```json
// Éxito
{
    "status": "success",
    "message": "Log enviado a cola"
}

// Error
{
    "detail": "Error message"
}
```