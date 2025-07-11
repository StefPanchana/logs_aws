from pymongo import MongoClient
from typing import List, Optional
from ...domain.entities.log import Log
from ...domain.repositories.log_repository import LogRepository
import os

class MongoDBRepository(LogRepository):
    _client = None
    
    def __init__(self):
        if MongoDBRepository._client is None:
            MongoDBRepository._client = MongoClient(
                os.getenv("MONGODB_URL", "mongodb://localhost:27017"),
                maxPoolSize=10,
                serverSelectionTimeoutMS=5000
            )
        
        self.db = MongoDBRepository._client[os.getenv("DATABASE_NAME", "logs_db")]
        self.collection = self.db[os.getenv("COLLECTION_NAME", "logs")]
    
    def save(self, log: Log) -> str:
        try:
            doc = {
                "level": log.level,
                "service": log.service,
                "message": log.message,
                "timestamp": log.timestamp,
                "metadata": log.metadata
            }
            print(f"💾 Guardando en MongoDB: {doc}")
            result = self.collection.insert_one(doc)
            print(f"✅ Guardado con ID: {result.inserted_id}")
            return str(result.inserted_id)
        except Exception as e:
            print(f"❌ Error guardando en MongoDB: {e}")
            raise
    
    def find_by_filters(self, service: Optional[str] = None, 
                       level: Optional[str] = None, 
                       limit: int = 100) -> List[Log]:
        query = {}
        if service:
            query["service"] = service
        if level:
            query["level"] = level
        
        docs = self.collection.find(query).sort("timestamp", -1).limit(limit)
        return [Log(
            id=str(doc["_id"]),
            level=doc["level"],
            service=doc["service"],
            message=doc["message"],
            timestamp=doc["timestamp"],
            metadata=doc.get("metadata")
        ) for doc in docs]