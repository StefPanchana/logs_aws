import redis
import json
from typing import Optional
from ...domain.entities.log import Log
from ...domain.repositories.queue_repository import QueueRepository
import os

class RedisRepository(QueueRepository):
    _client = None
    
    def __init__(self):
        if RedisRepository._client is None:
            RedisRepository._client = redis.from_url(
                os.getenv("REDIS_URL", "redis://localhost:6379"),
                max_connections=10,
                socket_timeout=5
            )
        
        self.client = RedisRepository._client
        self.queue_name = "logs_queue"
    
    def send(self, log: Log) -> bool:
        try:
            data = {
                "level": log.level,
                "service": log.service,
                "message": log.message,
                "timestamp": log.timestamp.isoformat(),
                "metadata": log.metadata
            }
            print(f"📤 Enviando a Redis: {data}")
            result = self.client.lpush(self.queue_name, json.dumps(data))
            print(f"✅ Enviado a Redis, queue size: {result}")
            return True
        except Exception as e:
            print(f"❌ Error enviando a Redis: {e}")
            return False
    
    def receive(self) -> Optional[Log]:
        try:
            data = self.client.brpop(self.queue_name, timeout=1)
            if data:
                log_data = json.loads(data[1])
                from datetime import datetime
                return Log(
                    level=log_data["level"],
                    service=log_data["service"],
                    message=log_data["message"],
                    timestamp=datetime.fromisoformat(log_data["timestamp"]),
                    metadata=log_data.get("metadata")
                )
        except:
            pass
        return None