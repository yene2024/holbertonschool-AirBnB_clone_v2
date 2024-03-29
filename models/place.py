#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""place_amenity table"""
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenity_ids'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60),  ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship("Review", backref="place", cascade="all, delete")


place_amenities = relationship('Place', secondary=amenity_place_association,
                               back_populates='amenity')

if getenv("HBNB_TYPE_STORAGE") == "db":
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)
    else:
        @property
        def amenities(self):
            """Returns the list of Amenity instances based on amenity_ids"""
            from models import storage
            return [storage.all(Amenity).get(id) for id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Handles append method for adding an Amenity.id to amenity_ids"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
