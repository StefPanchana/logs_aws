from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any

@dataclass
class Log:
    level: str
    service: str
    message: str
    timestamp: datetime
    metadata: Optional[Dict[str, Any]] = None
    id: Optional[str] = None