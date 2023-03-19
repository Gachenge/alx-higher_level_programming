#!/usr/bin/python3
"""
script that prints all Cioty objects from the database
takes three arguments: username, password and database name
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import State

if __name__ == "__main__":
    """
    print all city objects from the database
    sort in ascending order by cities.id
    print in format state name: city id city name
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3])
                           , echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for city, state in session.query(City, State) \
        .filter(City.state_id == State.id) \
            .order_by(City.id):
                print("{}: ({}) {}".format(state.name, city.id, city.name))
