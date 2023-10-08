from httpx import AsyncClient
from sqlalchemy import select
import pytest
from .conftest import async_session_maker


@pytest.mark.asyncio
async def test_task(ac: AsyncClient):
    response = await ac.post("/task", json={
        "x": 10,
        "y": 37,
        "operator": "*" 
    })
    assert response.status_code == 200

    task_id = response.json()["task_id"]
    response = await ac.get(f"/task/{task_id}")
    assert response.status_code == 200

    response = await ac.post("/task", json={
        "x": 21,
        "y": 0,
        "operator": "/" 
    })
    assert response.status_code == 422

    response = await ac.get("/task/dslkfp31")
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_tasks(ac: AsyncClient):
    response = await ac.get("/tasks")
    
    assert response.status_code == 200