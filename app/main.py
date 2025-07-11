from fastapi import FastAPI
from dotenv import load_dotenv
from app.container import Container
from app.presentation.api.routes import create_routes

load_dotenv()

def create_app() -> FastAPI:
    app = FastAPI(title="Microservicio de Logs", version="1.0.0")
    
    # Dependency Injection
    container = Container()
    
    # Routes
    router = create_routes(
        container.send_log_use_case,
        container.get_logs_use_case
    )
    app.include_router(router)
    
    @app.get("/health")
    async def health_check():
        try:
            # Test MongoDB
            container.log_repository.collection.find_one()
            # Test Redis
            container.queue_repository.client.ping()
            return {"status": "healthy", "service": "logs-microservice", "database": "logs_db.logs"}
        except:
            return {"status": "unhealthy", "service": "logs-microservice"}
    
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    import os
    
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    
    uvicorn.run(app, host=host, port=port)