#!/usr/bin/python3
""" List all states ordere by id """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    name = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(u, p, d)
    engine = create_engine(name)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State).filter(State.name.like('%a%')):
        session.delete(row)
    session.commit()
    session.close()
