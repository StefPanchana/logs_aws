from typing import List, Optional
from ...domain.entities.log import Log
from ...domain.repositories.log_repository import LogRepository

class GetLogsUseCase:
    def __init__(self, log_repository: LogRepository):
        self._log_repository = log_repository
    
    def execute(self, service: Optional[str] = None, 
                level: Optional[str] = None, 
                limit: int = 100) -> List[Log]:
        return self._log_repository.find_by_filters(service, level, limit)