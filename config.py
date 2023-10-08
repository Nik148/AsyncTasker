import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    CELERY_BACKEND_URL = os.environ.get('CELERY_BACKEND_URL')
    DB_URL = os.environ.get('DB_URL')

class TestConfig(Config):
    TEST_DB_URL = "postgresql+asyncpg://postgres:123@localhost:5432/test_tasks"
    TEST_DB_NAME = "test_tasks"
    TEST_CELERY_BACKEND_URL = "db+postgresql+psycopg2://postgres:123@localhost:5432/test_tasks"