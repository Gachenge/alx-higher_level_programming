#!/usr/bin/python3
"""
Script that adds state object Louisiana to thw database
takes three arguments: username, password, and database name
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    """
    insert a new object to the database 
    use sqlalchemy module
    print the new states.id
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    
    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    print(new.id)
