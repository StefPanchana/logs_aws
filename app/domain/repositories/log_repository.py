from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.log import Log

class LogRepository(ABC):
    @abstractmethod
    def save(self, log: Log) -> str:
        pass
    
    @abstractmethod
    def find_by_filters(self, service: Optional[str] = None, 
                       level: Optional[str] = None, 
                       limit: int = 100) -> List[Log]:
        pass