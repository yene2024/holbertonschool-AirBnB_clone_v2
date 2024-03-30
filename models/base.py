#!/user/bin/python3
import uuid
from datetime import datetime

class Base:
    """Base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if 'is_db' in kwargs:
            self.is_db = kwargs.pop('is_db')
        else:
            self.is_db = False

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.id = kwargs.pop('id', str(uuid.uuid4()))
            self.created_at = kwargs.pop('created_at', datetime.now())
            self.updated_at = kwargs.pop('updated_at', datetime.now())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        if self.is_db:
            # Perform operations specific to database storage
            pass
        else:
            # Perform operations specific to file storage
            pass

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
