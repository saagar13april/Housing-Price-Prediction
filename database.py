
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,Float,ForeignKey,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# we will create out users table

class Entry(Base):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True)
    bedrooms = Column(Integer)
    bathroom = Column(Integer)
    sqft_living = Column(Integer)
    view = Column(Integer)
    grade = Column(Integer)
    sqft_above = Column(Integer)
    sqft_basement = Column(Integer)
    lat = Column(Float)
    lng = Column(Float)
    sqft_living = Column(Integer)
    predicted_price = Column(Float)
    created_at = Column(DateTime,default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f"{self.id}"
    

def get_db():
    engine = create_engine('sqlite:///database.sqlite')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session



if __name__ == "__main__":
    engine = create_engine('sqlite:///database.sqlite')
    Base.metadata.create_all(engine)