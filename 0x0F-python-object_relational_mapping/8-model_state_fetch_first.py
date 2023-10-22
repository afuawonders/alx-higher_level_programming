#!/usr/bin/python3
"""
This script interacts with the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_all_states(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()

    if not states:
        print('No states found in the database.')
    else:
        for state in states:
            print(f'{state.id}: {state.name}')


def print_first_state(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).order_by(State.id).first()

    if instance is None:
        print('No states found in the database.')
    else:
        print(f'{instance.id}: {instance.name}')


if __name__ == "__main":
    if len(argv) != 4:
        print("Usage: {} username password database_name".format(argv[0]))
    else:
        db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
        engine = create_engine(db_uri)

        list_all_states(engine)
