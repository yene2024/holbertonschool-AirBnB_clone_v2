#!/usr/bin/python3
""" module for class State """
import models
import os
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class City(BaseModel, Base):
    """ class for City

        Attributs
        ===================

            name : name of City
                String, not null
            state_id: ForeignKey (class State), not null string
            place: relationship with class Place
    """
    __tablename__ = "cities"

    name = Column(
        String(128),
        nullable=True)
    state_id = Column(
        String(60),
        ForeignKey('states.id'),
        nullable=True)
    places = relationship(
        "Place", backref="cities",
        cascade="all, delete")
