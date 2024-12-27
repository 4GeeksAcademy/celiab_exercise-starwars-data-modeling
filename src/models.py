import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    favourites_user = relationship('Favourites', back_populates = 'user_favourites')

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    starship_id = Column(Integer, ForeignKey('starships.id'))

    user_favourites = relationship('User', back_populates = 'favourites_user')
    characters_fav = relationship('Characters', back_populates= 'favourite_characters')
    planets_fav = relationship('Planets', back_populates='favourite_planets')
    starships_fav = relationship('Starships', back_populates= 'favourite_starships')


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True,nullable = False)
    height = Column(String(50))
    favourite_characters = relationship('Favourites', back_populates= 'characters_fav')

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),unique=True,nullable=False)
    climate = Column(String(50)) 
    favourite_planets = relationship('Favourites', back_populates= 'planets_fav')


class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),unique=True ,nullable = False)
    favourite_starships = relationship('Favourites', back_populates= 'starships_fav')




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
