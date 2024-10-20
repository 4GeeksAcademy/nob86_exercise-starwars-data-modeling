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

    planet = relationship('Planets', back_populates='user')
    people = relationship('People', back_populates='user')

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

    user = relationship('User', back_populates='planets')
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
    people_id  = Column(Integer, ForeignKey('user.id'))
    favorite_id = Column(Integer, Foreingkey('favorite.people_id'))

    users = relationship('User', back_populates='people')
    favorites = relationship('Favorite', back_populates='people')

class Favorite(Base):
    __tablename__ = 'favorite'
    planets_id = Column(Integer, primary_key=True)
    people_id = Column(Integer, primary_key=True)

    planets = relationship('Planets', back_populates='favorite')
    peoples = relationship('People', back_populates='favorite')

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
