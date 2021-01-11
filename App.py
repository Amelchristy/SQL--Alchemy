from flask import Flask, jsonify
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.pool import StaticPool


# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={"check_same_thread": False}, poolclass=StaticPool, echo=True)
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save References to Each Table
Measurement = Base.classes.measurement
Station = Base.classes.station


session = Session(engine)

# Flask Setup
app = Flask(__name__)


# Flask Routes:

# Home Route
@app.route("/")
def welcome():
        return """<html>
<h1>Hawaii Climate Flask App</h1>
<img src="https://www.johnnyjet.com/wp-content/uploads/2020/12/hawaii-move.jpg" alt="Hawaii Weather"/>
<p><b>Precipitation Analysis:</b></p>
<a href="/api/v1.0/precipitation">Precipitation</a>

<br>
<p><b>Station Analysis:</b></p>
<a href="/api/v1.0/stations">Stations List</a>

<br>
<p><b>Temperature Analysis:</b></p>
<a href="/api/v1.0/tobs">Tobs at Station USC00519281 </a>

<br>
<p><b>Start Day Analysis:</b></p>
<a href="/api/v1.0/2017-08-12">2017-08-12</a>

<p><b>Start & End Day Analysis:</b></p>

<a href="/api/v1.0/2017-08-12/2017-08-26">2017-08-12 --- 2017-08-26</a>
</html>
"""

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
        one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
        
        prcp_data = session.query(Measurement.date, Measurement.prcp).\
                filter(Measurement.date >= one_year_ago).\
                order_by(Measurement.date).all()
        
        prcp_data_list = dict(prcp_data)
       
        return jsonify(prcp_data_list)

# Station Route
@app.route("/api/v1.0/stations")
@app.route("/api/v1.0/tobs")
def tobs():
        one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
       
        tobs_data = session.query(Measurement.date, Measurement.tobs).\
                filter(Measurement.date >= one_year_ago).\
                filter(Measurement.station == "USC00519281").\
                order_by(Measurement.date).all()
        
        tobs_data_list = list(tobs_data)
       
        return jsonify(tobs_data_list)

# Start Day Route
@app.route("/api/v1.0/<start>")
def start_day(start):
        start_day = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).\
                group_by(Measurement.date).all()
       
        start_day_list = list(start_day)
        
        return jsonify(start_day_list)

# Start-End Day Route
@app.route("/api/v1.0/<start>/<end>")
def StartEnd(start, end):
        StartEnd = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).\
                filter(Measurement.date <= end).\
                group_by(Measurement.date).all()
       
        StartEndList = list(StartEnd)
        
        return jsonify(StartEndList)


if __name__ == '__main__':
    app.run(debug=True)