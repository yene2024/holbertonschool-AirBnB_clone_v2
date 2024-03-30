#!/usr/bin/python3
""" Place Module for HBNB project """
<<<<<<< HEAD
import models
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))
=======
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

"""place_amenity table"""
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenity_ids'),
                             primary_key=True, nullable=False))
>>>>>>> f23f70016d2a7dc533eb97b7479b5aa4ff071205


class Place(BaseModel, Base):
    """ A place to stay """
<<<<<<< HEAD
    __tablename__ = 'places'
=======

    __tablename__ = "places"

>>>>>>> f23f70016d2a7dc533eb97b7479b5aa4ff071205
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
<<<<<<< HEAD
    description = Column(String(1024), nullable=True)
=======
    description = Column(String(1024))
>>>>>>> f23f70016d2a7dc533eb97b7479b5aa4ff071205
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
<<<<<<< HEAD
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """Getter attribute reviews that returns
            the list of Review instances"""
            review_list = []
            all_reviews = models.storage.all(Review)
            for revs in all_reviews.values():
                if revs.place_id == self.id:
                    review_list.append(revs)
            return review_list

        @property
        def amenities(self):
            """Getter attribute amenities that returns
            the list of Amenity instances"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, value):
            """Setter attribute amenities that handles
            append method for adding an Amenity.id
            to the attribute amenity_ids"""
            if type(value).__name__ == "Amenity":
                self.amenity_ids.append(value.id)

=======
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship("Review", backref="place", cascade="all, delete")


place_amenities = relationship('Place', back_populates='amenity')
>>>>>>> f23f70016d2a7dc533eb97b7479b5aa4ff071205
