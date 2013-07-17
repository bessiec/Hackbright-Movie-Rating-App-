from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker


ENGINE = None
Session = None

Base = declarative_base()

### Class declarations go here

class User(Base):
    __tablename__ ="users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable=True)
    password = Column(String(65), nullable=True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)
    gender = Column(String(3), nullable=True)
    profession = Column(String(70), nullable=True)

class Movies(Base):
    __tablename__="movies"

    id = Column(Integer, primary_key = True)
    name = Column(String(64), nullable=True)
    released_at = Column(DateTime, nullable=True) #we need to convert/import Datetime later 
    imdb_url = Column(String(120), nullable=True)


class Ratings(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key = True)
    movie_id = Column(Integer, nullable = True)
    user_id = Column(Integer, nullable = True)
    rating = Column(Integer, nullable = True) # can only be from 1-5
    # unknown = Column(Integer, nullable = True)
    

### End class declarations

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
