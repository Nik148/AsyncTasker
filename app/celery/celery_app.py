from celery import Celery
from config import Config


celery = Celery(__name__,
                broker=Config.CELERY_BROKER_URL,
                backend=Config.CELERY_BACKEND_URL,
                timezone = "Europe/Kiev",
                result_extended=True,
                task_serializer = 'json',
                result_serializer = 'json',
                database_table_names = {
                    'task': 'task',
                    'group': 'task_group',
                },
                )