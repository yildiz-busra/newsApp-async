from sqlalchemy import Column, Integer, String
from database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    link = Column(String, unique=True, index=True)
    date = Column(String)
    category = Column(String)
    description = Column(String)
    full_text = Column(String)
    
