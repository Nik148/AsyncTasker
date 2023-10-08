from config import TestConfig, Config
from celery import Celery


celery = Celery(__name__,
                broker=Config.CELERY_BROKER_URL,
                backend=TestConfig.TEST_CELERY_BACKEND_URL,
                CELERY_ALWAYS_EAGER=True,
                timezone = "Europe/Kiev",
                result_extended=True,
                task_serializer = 'json',
                result_serializer = 'json',
                database_table_names = {
                    'task': 'task',
                    'group': 'task_group',
                },
                include=("app.celery.celery_task",)
                )