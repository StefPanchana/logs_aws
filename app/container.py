from .infrastructure.database.mongodb_repository import MongoDBRepository
from .infrastructure.queue.redis_repository import RedisRepository
from .application.use_cases.send_log import SendLogUseCase
from .application.use_cases.get_logs import GetLogsUseCase
from .application.use_cases.process_log import ProcessLogUseCase

class Container:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        # Repositories
        self.log_repository = MongoDBRepository()
        self.queue_repository = RedisRepository()
        
        # Use Cases
        self.send_log_use_case = SendLogUseCase(self.queue_repository)
        self.get_logs_use_case = GetLogsUseCase(self.log_repository)
        self.process_log_use_case = ProcessLogUseCase(self.queue_repository, self.log_repository)
        
        self._initialized = True