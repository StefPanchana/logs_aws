import requests
import json
from datetime import datetime

def test_logs_endpoint():
    url = "http://localhost:8000/logs"
    
    payload = {
        "level": "INFO",
        "service": "test_service",
        "message": "Test log message",
        "metadata": {
            "test_id": "test_123",
            "timestamp": datetime.utcnow().isoformat()
        }
    }
    
    try:
        print(f"🚀 Enviando POST a {url}")
        print(f"📦 Payload: {json.dumps(payload, indent=2)}")
        
        response = requests.post(url, json=payload, timeout=10)
        
        print(f"📊 Status Code: {response.status_code}")
        print(f"📋 Response: {response.text}")
        
        if response.status_code == 200:
            print("✅ API funcionando correctamente")
        else:
            print("❌ API retornó error")
            
    except requests.exceptions.ConnectionError:
        print("❌ No se puede conectar al API - ¿Está corriendo el servidor?")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_health_endpoint():
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        print(f"🏥 Health Check: {response.json()}")
    except Exception as e:
        print(f"❌ Health Check Error: {e}")

if __name__ == "__main__":
    print("🧪 Probando API...")
    test_health_endpoint()
    test_logs_endpoint()