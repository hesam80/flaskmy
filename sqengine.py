from flask import Flask
import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:artists.db:', echo=True)
#app=Flask(__name__)
print(sqlalchemy.__version__ )
Engine.connect()



