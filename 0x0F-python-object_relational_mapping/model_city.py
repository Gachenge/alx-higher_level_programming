#!/usr/bin/python3
"""
defines the city class
class city inherits from Base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String

Base = declarative_base()


class City(Base):
    """links to the mysql table cities

    Args:
        id: primary key integer
        name: cant be null max 128 characters
        state_id: integer cant be null and is a foreign key
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
