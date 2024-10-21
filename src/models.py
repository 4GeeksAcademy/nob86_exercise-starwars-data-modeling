import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    emailadress = Column(String(50), nullable=False)
    suscription_data = Column(String(50), nullable=False)
    birthdate = Column(Integer, nullable=False)

    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    climate = Column(String)
    population = Column(Integer)
    created = Column(Integer)
    diameter = Column(Integer)
    gravity = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    surface_water = Column(Integer)
    terrain = Column(String)
    planets_id = Column(Integer, ForeignKey('user.id',))
    favorite = Column(Integer, ForeignKey('favorite.planets_id'))

    # user = relationship('User', back_populates='planets')
    favorite = relationship('Favorite', back_populates='planets')

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String)
    skin_color = Column(String)
    eyes_coloe = Column(String)
    birthdate = Column(Integer)
    gender = Column(String)
    

   
    favorites = relationship('Favorite', back_populates='people')

class Favorite(Base):
    __tablename__ = 'favorite'
    planets_id = Column(Integer, ForeignKey('planets.id'), primary_key=True, nullable=True)
    people_id = Column(Integer, ForeignKey('people.id'), primary_key=True, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True, nullable=False)

    planets = relationship('Planets', back_populates='favorite')
    peoples = relationship('People', back_populates='favorite')



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
