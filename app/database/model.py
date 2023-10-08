from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.postgresql import BYTEA
from .core import Base
import pickle


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(String(155))
    status = Column(String(50))
    result = Column(BYTEA)
    date_done = Column(DateTime)
    traceback = Column(Text)
    name = Column(String(155))
    args = Column(BYTEA)
    kwargs = Column(BYTEA)
    worker = Column(String)
    retries = Column(Integer)
    queue = Column(String)

    def get_result(self):
        return pickle.loads(self.result, encoding='utf-8')