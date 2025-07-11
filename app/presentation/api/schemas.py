from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class LogRequest(BaseModel):
    level: str
    service: str
    message: str
    metadata: Optional[Dict[str, Any]] = None

class LogResponse(BaseModel):
    id: Optional[str]
    level: str
    service: str
    message: str
    timestamp: datetime
    metadata: Optional[Dict[str, Any]] = None