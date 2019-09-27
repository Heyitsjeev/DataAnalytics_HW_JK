import datetime as dt
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

lastTwelveMonths = '2016-08-24'

@app.route("/")
def welcome():
    return (
        f"<p>Welcome to the Hawaii weather API!</p>"
        f"<p>Usage:</p>"
        f"/api/v1.0/precipitation<br/>Returns a JSON list of percipitation data for the dates between 8/24/16 and 8/23/17<br/><br/>"
        f"/api/v1.0/stations<br/>Returns a JSON list of the weather stations<br/><br/>"
        f"/api/v1.0/tobs<br/>Returns a JSON list of the Temperature Observations (tobs) for each station for the dates between 8/23/16 and 8/23/17<br/><br/>"
        f"/api/v1.0/date<br/>Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates between the given start date and 8/23/17<br/><br/>."
        f"/api/v1.0/start_date/end_date<br/>Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates between the given start date and end date<br/><br/>."
    )

 # /api/v1.0/precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    precip = session.query(Measurement.date, func.avg(Measurement.prcp)).filter(Measurement.date >= lastTwelveMonths).group_by(Measurement.date).all()
    return jsonify(precip)


# # /api/v1.0/stations
@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Station.station, Station.name).all()
    return jsonify(stations)


 # /api/v1.0/tobs
@app.route("/api/v1.0/tobs")
def tobs():
    tobss = session.query(Measurement.date, Measurement.station, Measurement.tobs).filter(Measurement.date >= lastTwelveMonths).all()
    return jsonify(tobss)


 # /api/v1.0/<start>/<end>
@app.route("/api/v1.0/<start>/<end>")
def startDateEndDate(start,end):
    startAndEndDay = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    return jsonify(startAndEndDay)

if __name__ == "__main__":
    app.run(debug=True)