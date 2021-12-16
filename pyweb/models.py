from sqlalchemy import Column, String, Integer
from pyweb.init_db import Base

class Message(Base):
    __tablename__ = 'Message'

    id = Column(Integer, primary_key=True)
    content = Column(String)

    def __init__(self, content=None):
        self.content = content