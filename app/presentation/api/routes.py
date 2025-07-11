from fastapi import APIRouter, HTTPException
from typing import List, Optional
from .schemas import LogRequest, LogResponse
from ...application.use_cases.send_log import SendLogUseCase
from ...application.use_cases.get_logs import GetLogsUseCase

router = APIRouter()

def create_routes(send_log_use_case: SendLogUseCase, get_logs_use_case: GetLogsUseCase):
    
    @router.post("/logs")
    async def send_log(log_request: LogRequest):
        try:
            success = send_log_use_case.execute(
                log_request.level,
                log_request.service,
                log_request.message,
                log_request.metadata
            )
            if success:
                return {"status": "success", "message": "Log enviado a cola"}
            raise HTTPException(status_code=500, detail="Error enviando log")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    @router.get("/logs", response_model=List[LogResponse])
    async def get_logs(service: Optional[str] = None, 
                      level: Optional[str] = None, 
                      limit: int = 100):
        try:
            logs = get_logs_use_case.execute(service, level, limit)
            return [LogResponse(
                id=log.id,
                level=log.level,
                service=log.service,
                message=log.message,
                timestamp=log.timestamp,
                metadata=log.metadata
            ) for log in logs]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    

    
    return router