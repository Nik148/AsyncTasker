from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.routers import router

tags_metadata = [
    {
        "name": "Task",
        "description": "Операции с фоновыми задачами",
    }
]

app = FastAPI(openapi_tags=tags_metadata)

app.include_router(router)


Instrumentator().instrument(app=app).expose(app)