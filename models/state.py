#!/usr/bin/python3
""" State Module for HBNB project """


import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            "City",
            backref="states",
            cascade="all, delete, delete-orphan"
        )
    else:
        @property
        def cities(self):
            """ Getter cities """
            list_city = []
            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    list_city.append(City)
            return list_city
