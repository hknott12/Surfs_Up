import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Access the database
engine = create_engine("sqlite:///hawaii.sqlite")
#Reflect database
Base = automap_base()
#Reflect tables
Base.prepare(engine, reflect=True)
#Save references
Measurement = Base.classes.measurement
Station = Base.classes.station
#Create session link
session = Session(engine)

#Set Up Flask
#define app
app = Flask(__name__)