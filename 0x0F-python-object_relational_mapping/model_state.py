#!/usr/bin/python3
"""
python file that contains class definition of a state
state:
    inherits from Base
    links to mysql table
    class attributes id and name
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """
    inherits from Base
    table name is states
    attributes:
        id: unique integer, can't be null and is primary key
        name: string with max 123 char and can't be null
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
