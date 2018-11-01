import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from database_setup import Base, Blog, User
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///blog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

post = session.query(Blog).filter_by(id =12 ).one()
post.user_id = 2
session.commit()

