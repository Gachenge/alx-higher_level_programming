#!/usr/bin/python3
"""
prints the object with the name passed as argument
must import sqlalchemy
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    """
    takes four arguments, username, password, database name and statename
    return 'Not Found if there is no id
    search through the session
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print(state.id)
            found = True
            break
    if not found:
        print("Not found")
