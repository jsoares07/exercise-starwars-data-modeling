import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(120), ForeignKey('person.name'), nullable=False)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__= 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    planets_id= Column(Integer, ForeignKey('planets.id'))
    vehicles_id= Column(Integer, ForeignKey('vehicles.id'))
    starships_id= Column(Integer, ForeignKey('starships.id'))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer,primary_key=True)
    name = Column(String(120), nullable=False)
    eye_color = Column(String(120), nullable=False)
    planets_id= Column(Integer, ForeignKey('planets.id'))
    vehicles_id= Column(Integer, ForeignKey('vehicles.id'))
    starships_id= Column(Integer, ForeignKey('starships.id'))
    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer,primary_key=True)
    name = Column(String(120), nullable=False)
    diameter = Column(Integer)
    population = Column(Integer)
    characters = relationship(Characters)
 
class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    model = Column(String(120), nullable=False)
    crew = Column(Integer)
    characters = relationship(Characters)

class Starships(Base):
    __tablename__ ='starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    model = Column(String(120), nullable=False)
    characters_id= Column(Integer, ForeignKey('characters.id'))
    length = Column(Integer)
    characters = relationship(Characters)




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')