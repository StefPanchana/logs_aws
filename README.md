# Microservicio de Logs

Arquitectura: **Microservicios** → **[Cola Redis/SQS]** → **[Microservicio Logs]** → **[MongoDB]**

## Componentes
- **API REST** (FastAPI) - Recibe logs y los envía a cola
- **Worker** - Procesa logs de la cola y los guarda en MongoDB
- **Redis/SQS** - Sistema de colas
- **MongoDB** - Base de datos de logs

## Uso

### Desarrollo Local
```bash
pip install -r requirements.txt
docker-compose up -d redis mongodb
python main.py  # API en puerto 8000
python worker.py  # Worker en segundo plano
```

### Docker
```bash
docker-compose up
```

### Enviar Logs
```bash
curl -X POST http://localhost:8000/logs \
  -H "Content-Type: application/json" \
  -d '{"level":"INFO","service":"test","message":"Test log"}'
```

### Consultar Logs
```bash
curl http://localhost:8000/logs?service=test&level=INFO
```
