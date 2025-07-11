import requests
import os
from datetime import datetime
from typing import Dict, Any

class InteractionLogger:
    def __init__(self, service_url: str = None):
        self.base_url = service_url or os.getenv("LOGS_SERVICE_URL", "http://localhost:8000")
        self.service_name = "core_aws"
        self.timeout = 5
    
    def log_event(self, event_type: str, session_id: str, **kwargs) -> bool:
        """Log interaction events to logs microservice"""
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
            
            response = requests.post(
                f"{self.base_url}/logs", 
                json=payload, 
                timeout=self.timeout
            )
            return response.status_code == 200
        except Exception:
            return False
    
    def _get_log_level(self, event_type: str) -> str:
        level_map = {
            "query_start": "INFO",
            "model_attempt": "DEBUG", 
            "response_generated": "INFO",
            "error": "ERROR",
            "warning": "WARN"
        }
        return level_map.get(event_type, "INFO")