from sqlalchemy import Column, String, Integer, DATETIME
from db import Base
from sqlalchemy.sql import func


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(250))
    description = Column(String)
    created_at = Column(DATETIME(timezone=True), server_default=func.now())

    def __str__(self):
        return self.title
