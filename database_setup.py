import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	username = Column(String(50), nullable=False)
	email = Column(String(250), nullable=False)
	pw_hash = Column(String(250), nullable=False)

	


class Blog(Base):
	__tablename__ = 'blog'

	id = Column(Integer, primary_key=True)
	titulo = Column(String(50), nullable=False)
	contenido = Column(String(250), nullable=False)
	fecha_creacion = Column(DateTime, nullable=False)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)



engine = create_engine('postgresql://god:METAL@localhost/mbdb')
Base.metadata.create_all(engine)
