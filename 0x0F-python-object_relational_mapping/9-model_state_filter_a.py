#!/usr/bin/python3
"""
This script lists all State objects that contain the letter `a`
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states_with_letter_a(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%'))

    for state in states:
        print(f'{state.id}: {state.name}')


if __name__ == "__main":
    if len(argv) != 4:
        print("Usage: {} username password database_name".format(argv[0]))
    else:
        db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
        engine = create_engine(db_uri)

        list_states_with_letter_a(engine)
