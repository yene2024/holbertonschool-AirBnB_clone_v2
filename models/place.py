#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=True)
    user_id = Column(String(60),  ForeignKey('users.id'), nullable=True)
    name = Column(String(128), nullable=True)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=True)
    number_bathrooms = Column(Integer, nullable=True)
    max_guest = Column(Integer, nullable=True)
    price_by_night = Column(Integer, nullable=True)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship("Review", backref="place", cascade="all, delete")

    @property
    def review(self):
        """Return a list of reviews"""
        list_reviews = storage.all(Review)
        place_reviews = [review for review in list_reviews.values()
                         if review.place_id == self.id]
        return place_reviews
