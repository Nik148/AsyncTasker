from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select
from typing import List
from app.schema import CreateTaskRequest, CreateTaskResponse, GetTaskResponse, GetTasksResponse
from app.celery.celery_task import calculate
from app.database.core import get_session
from app.database.model import Task
from app.doc import *


router = APIRouter(prefix="", tags=["Task"])


@router.post("/task", response_model=CreateTaskResponse, description=create_task_description)
async def create_task(data: CreateTaskRequest):
    task_id = calculate.delay(data.x, data.y, data.operator)
    return task_id

@router.get("/task/{task_id}", response_model=GetTaskResponse, description=get_task_description)
async def get_task(task_id: str, session: AsyncSession = Depends(get_session)):
    # task = calculate.AsyncResult(task_id)
    task = await session.execute(select(Task).where(Task.task_id==task_id))
    task: Task = task.scalar()
    if not task:
        return JSONResponse(status_code=404, content={"message": "Задача не найдена"})
    if task.status != "SUCCESS":
        return JSONResponse(status_code=404, content={"message": "Задача в процессе выполнения"})

    return {"result": task.get_result()}

@router.get("/tasks", response_model=List[GetTasksResponse], description=get_tasks_description)
async def get_tasks(session: AsyncSession = Depends(get_session)):
    tasks = await session.execute(select(Task))
    tasks: List[Task] = tasks.scalars().all()
    return tasks