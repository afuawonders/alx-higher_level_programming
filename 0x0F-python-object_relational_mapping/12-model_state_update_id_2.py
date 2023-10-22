#!/usr/bin/python3
"""
This script changes the name of a State object
from the database 'hbtn_0e_6_usa'.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def change_state_name(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    ari_state = session.query(State).filter_by(id=2).first()
    if ari_state:
        ari_state.name = 'New Mexico'
        session.commit()
        session.close()
    else:
        print('State with ID 2 not found')


if __name__ == "__main":
    if len(argv) != 4:
        print("Usage: {} username password database_name".format(argv[0]))
    else:
        db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
        engine = create_engine(db_uri)
        change_state_name(engine)
