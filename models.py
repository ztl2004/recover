from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger, Text

Base = declarative_base()

class Rat(Base):
    __tablename__ = 'rats'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    title = Column(String(100))

    def __init__(self, name, title):
        self.name = name
        self.title = title 

    def __repr__(self):
        return "<Rat('%s','%s')>" % (self.name, self.title) 

class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    title = Column(String(500))
    location = Column(String(500))
    content = Column(Text)

    
    def __init__(self, name):
        self.title = title
        self.location = location
        self.content = content
    
    def __repr__(self):
        return "<Event('%s')>" % (self.title)

