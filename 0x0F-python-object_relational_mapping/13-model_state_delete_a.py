#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database 'hbtn_0e_6_usa'.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_states_with_letter_a(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).filter(State.name.contains('a')):
        session.delete(instance)
    session.commit()
    session.close()


if __name__ == "__main":
    if len(argv) != 4:
        print("Usage: {} username password database_name".format(argv[0]))
    else:
        db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
        engine = create_engine(db_uri)
        delete_states_with_letter_a(engine)
