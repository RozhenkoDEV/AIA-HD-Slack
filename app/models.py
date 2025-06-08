from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
import datetime

Base = declarative_base()

class Prompt(Base):
    __tablename__ = "prompts"
    id = Column(Integer, primary_key=True, index=True)
    tag = Column(String, unique=True)
    content = Column(Text)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
