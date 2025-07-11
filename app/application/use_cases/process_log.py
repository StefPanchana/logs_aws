from ...domain.repositories.log_repository import LogRepository
from ...domain.repositories.queue_repository import QueueRepository

class ProcessLogUseCase:
    def __init__(self, queue_repository: QueueRepository, log_repository: LogRepository):
        self._queue_repository = queue_repository
        self._log_repository = log_repository
    
    def execute(self) -> bool:
        log = self._queue_repository.receive()
        if log:
            self._log_repository.save(log)
            return True
        return False