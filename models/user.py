#!/usr/bin/python3
"""This module defines a class User"""
import models
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = db.Column(String(128), nullable=False)
    password = db.Column(String(128), nullable=False)
    first_name = db.Column(String(128))
    last_name = db.Column(String(128))
    
    places = relationship("Place", backref="user", cascade="delete")
