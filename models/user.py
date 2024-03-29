#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=True)
    password = Column(String(128), nullable=True)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship("Place", backref="user",
                          cascade="all, delete")
