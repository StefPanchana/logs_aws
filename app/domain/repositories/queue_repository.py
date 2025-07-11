from abc import ABC, abstractmethod
from typing import Optional
from ..entities.log import Log

class QueueRepository(ABC):
    @abstractmethod
    def send(self, log: Log) -> bool:
        pass
    
    @abstractmethod
    def receive(self) -> Optional[Log]:
        pass