from sqlalchemy import DATETIME, Column, Integer, String
from sqlalchemy.sql import func

from db import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(250))
    description = Column(String)
    created_at = Column(DATETIME(timezone=True), server_default=func.now())

    def __str__(self):
        return self.title
