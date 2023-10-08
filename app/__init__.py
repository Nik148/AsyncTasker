from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.routers import router


app = FastAPI()

app.include_router(router)


Instrumentator().instrument(app=app).expose(app)