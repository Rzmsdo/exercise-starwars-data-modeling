import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, unique=True)
    users_nick_name = Column(String(50), unique=True, nullable=False)
    users_name = Column(String)
    users_last_name = Column(String)
    users_email = Column(String, unique=True, nullable=False)
    users_password = Column(String)
    users_phone = Column(String, unique=True, nullable=False)
    users_address = Column(String)
    users_subs_date = Column(String)
    
class StartSession(Base):
    __tablename__ = 'startsession'
    id = Column(Integer, primary_key=True)
    user_email =Column(String, ForeignKey('usuarios.user_email'))
    user_password =Column(String, ForeignKey('usuarios.user_password'))
    last_session = Column(String)

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    color_eyes = Column(String)
    color_skin = Column(String)
    age = Column(Integer)
    mass = Column(Integer)

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    pers_id = Column(Integer, ForeignKey('personaje.id'))
    pers_name = Column(String, ForeignKey('personaje.name'))
    pers_last_name= Column(String, ForeignKey('personaje.last_name'))

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    descrption = Column(String)
    radio = Column(Integer)
    terrain = Column(String)

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    planeta_id =Column(Integer, ForeignKey('planeta.id'))
    planeta_name = Column(String, ForeignKey('planeta.name'))
    planeta_radio = Column(Integer, ForeignKey('planeta.radio'))


class Favoritos(Base):
    __tablename__='favoritos'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('usuarios.user_id'))
    favorito_planeta = Column(Integer, ForeignKey('planeta.id'))
    favorito_personaje= Column(Integer, ForeignKey('personaje.id'))



    


    

    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
