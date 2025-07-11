import requests
import os
from datetime import datetime
from typing import Optional, Dict, Any

class InteractionLogger:
    def __init__(self):
        self.base_url = os.getenv("LOGS_SERVICE_URL", "http://localhost:8000")
        self.service_name = "core_aws"
    
    def log_event(self, event_type: str, session_id: str, **kwargs):
        """Log interaction events from core_aws microservice"""
        try:
            payload = {
                "level": self._get_log_level(event_type),
                "service": self.service_name,
                "message": f"{event_type}: {session_id}",
                "metadata": {
                    "event_type": event_type,
                    "session_id": session_id,
                    "timestamp": datetime.utcnow().isoformat(),
                    **kwargs
                }
            }
            
            response = requests.post(f"{self.base_url}/logs", json=payload, timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def _get_log_level(self, event_type: str) -> str:
        """Map event types to log levels"""
        level_map = {
            "query_start": "INFO",
            "model_attempt": "DEBUG", 
            "response_generated": "INFO",
            "error": "ERROR",
            "warning": "WARN"
        }
        return level_map.get(event_type, "INFO")