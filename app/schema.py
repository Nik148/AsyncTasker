from pydantic import BaseModel, root_validator
from enum import Enum
from operator import add, sub, mul, truediv
from typing import Union

operator = {"+": add,
            "-": sub,
            "*": mul,
            "/": truediv}

class Operator(str, Enum):
    summation = "+"
    difference = "-"
    multiplication = "*"
    division = "/"

class CreateTaskRequest(BaseModel):
    x: int
    y: int
    operator: Operator

    @root_validator(pre=True)
    def formatedField(cls, v):
        if v["operator"] == Operator.division and v["y"] == 0:
            raise ValueError("На ноль делить нельзя")
        return v

class CreateTaskResponse(BaseModel):
    task_id: str

class GetTaskResponse(BaseModel):
    result: Union[int, float]

class GetTasksResponse(BaseModel):
    task_id: str
    status: str

    class Config:
        from_attributes = True