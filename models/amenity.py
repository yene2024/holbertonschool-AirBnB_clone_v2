#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeingKey
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenity_ids'),
                             primary_key=True, nullable=False))

class Amenity(BaseModel, Base):
    """This represents amenities"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Amenity', secondary=place_amenity,
                                   backref="amenities")
