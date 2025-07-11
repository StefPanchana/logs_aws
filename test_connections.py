import os
from dotenv import load_dotenv
from pymongo import MongoClient
import redis

load_dotenv()

def test_mongodb():
    try:
        client = MongoClient(os.getenv("MONGODB_URL", "mongodb://localhost:27017"))
        db = client[os.getenv("DATABASE_NAME", "logs_db")]
        collection = db[os.getenv("COLLECTION_NAME", "logs")]
        
        # Test insert
        test_doc = {"test": "connection", "status": "ok"}
        result = collection.insert_one(test_doc)
        print(f"✅ MongoDB conectado - ID: {result.inserted_id}")
        
        # Test find
        doc = collection.find_one({"_id": result.inserted_id})
        print(f"✅ MongoDB lectura OK - Doc: {doc}")
        
        # Cleanup
        collection.delete_one({"_id": result.inserted_id})
        print("✅ MongoDB test completado")
        
    except Exception as e:
        print(f"❌ MongoDB Error: {e}")

def test_redis():
    try:
        client = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))
        client.ping()
        print("✅ Redis conectado")
    except Exception as e:
        print(f"❌ Redis Error: {e}")

if __name__ == "__main__":
    print("🔍 Probando conexiones...")
    test_mongodb()
    test_redis()