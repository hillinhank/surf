# 9.5.1 add dependencies
import datetime as dt
import numpy as np
import pandas as pd
# import SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# import flask dependencies
from flask import Flask, jsonify

# set up db engine
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect db into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# save our references
Measurement = Base.classes.measurement
Station = Base.classes.station

# create our seesion link
session = Session(engine)

# define our flask app
app = Flask(__name__)

# 9.5.2 - create our flask routs
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# 9.5.3 precip route and jsonify the data
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

#### 9.4.1, 9.4.2 and 9.4.3 - flask app
# from flask import Flask
#### create an instance
# app = Flask(__name__)
#### create route - define a starting point
# @app.route('/')
#### create a function for the root
# def hello_world():
#     return 'Hello World'
#### navigate to folder in terminal and run: export FLASK_APP=app.py
#### followed by: flask run