#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # @property
    # def cities(self):
    #     """Getter attribute cities that
    # returns the list of City instances"""
    #     city_list = []
    #     all_cities = models.storage.all(City)
    #     for city in all_cities.values():
    #         if city.state_id == self.id:
    #             city_list.append(city)
    #     return city_list

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Returns the list of City instances with
            state_id equals to the current State.id"""
            import models
            all_cities = models.storage.all(City)
            return [city for city in all_cities.values()
                    if city.state_id == self.id]
