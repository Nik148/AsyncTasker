from .celery_app import celery
from app.schema import operator, Operator

@celery.task()
def calculate(x: int, y: int, oper: Operator):
    return operator[oper](x, y)