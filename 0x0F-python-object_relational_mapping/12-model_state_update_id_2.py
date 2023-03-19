#!/usr/bin/python3
"""
script that changes the name of a state object
takes three arguments: username, password, database name
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    """
    use sqlalchemy to change the name of an object
    change name of object.id 2 to New Mexico
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if state.id == 2:
            state.name = "New Mexico"
    session.commit()
