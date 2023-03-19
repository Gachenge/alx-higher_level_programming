#!/usr/bin/python3
"""
script that lists all State objects that contain the letter a
takes three arguments: username, password and database name
script should not be executed when imported
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    """
    use sqlalchemy
    results should be stored in ascending order
    filter results that contain the letter 'a'
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
