from datetime import datetime
from ...domain.entities.log import Log
from ...domain.repositories.queue_repository import QueueRepository

class SendLogUseCase:
    def __init__(self, queue_repository: QueueRepository):
        self._queue_repository = queue_repository
    
    def execute(self, level: str, service: str, message: str, metadata: dict = None) -> bool:
        log = Log(
            level=level,
            service=service,
            message=message,
            timestamp=datetime.utcnow(),
            metadata=metadata
        )
        return self._queue_repository.send(log)