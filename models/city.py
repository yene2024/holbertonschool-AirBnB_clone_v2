from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

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
