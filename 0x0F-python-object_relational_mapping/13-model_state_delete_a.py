#!/usr/bin/python3
"""
script that deletes all state objects with a name containing 'a'
code should not be executed when imported
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    """
    takes in 3 arguments: username, password and database
    you must use sqlalchemy search and destroy
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if 'a' in state.name:
            session.delete(state)
    session.commit()
