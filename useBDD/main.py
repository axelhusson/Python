# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sqlite3

import connexion as connexion
from sqlalchemy import Column, Integer, Unicode, UnicodeText, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from random import choice
#from string import letters


engine = create_engine('sqlite:database.db', echo=True)
Base = declarative_base(bind=engine)

class Player(Base):
    __tablename__ ='player'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(40))
    level = Column(Integer)
    classe = Column(String(20))

    def __init__(self, name, level=None, classe=None):
        self.name = name
        self.level = level
        self.classe = classe

Base.metadata.create_all()

Session = sessionmaker(bind=engine)
s = Session()

#u = Player(Axel)

connexion.close()