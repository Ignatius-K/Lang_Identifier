from database.db import BASE
from sqlalchemy import Column, Integer, String, Text


class Log(BASE):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    lang = Column(String)
