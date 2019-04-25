import numpy as np
import datetime
import datetime as dt
import datetime as datetime
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<p>Welcome to Hawaii Weather Climate Analysis and Exploration</br></p>"
        f"<p>Available routes are:<br/></p>"
        f"<a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>/api/v1.0/stations</a><br/>"
        f"<a href='/api/v1.0/tobs'>/api/v1.0/tobs</a><br/>"
        f"<p>JSON list of the minimum temperature, the average temperature, and the max temperature for a given start:<br/>"
        f"<a href='/api/v1.0/2017-01-01'>/api/v1.0/2017-01-01</a><br></p>"
        f"<p>JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end range:<br/>"
        f"<a href='/api/v1.0/2017-01-01/2017-01-07'>/api/v1.0/2017-01-01/2017-01-07</a></p>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of dates and precipitation value"""

    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

# Perform a query to retrieve the data and precipitation scores

    Precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > last_year).\
    order_by(Measurement.date).all()

    # Create a dictionary from the row data and append to a list of all_dates
    
    all_dates = []
    for date, prcp in Precipitation:
        dtprp_dict = {}
        dtprp_dict["date"] = date
        dtprp_dict["precipitation"] = prcp
        all_dates.append(dtprp_dict)

    return jsonify(all_dates)


@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset"""

    # Query all stations
    station_query = session.query(Measurement.station).group_by(Measurement.station).all()

    # Create a dictionary from the row data and append to a list of all_dates
    all_stations = []
    for station in station_query:
        all_stations.append(station)
    
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of Temperature Observations (tobs) for the previous year"""
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    temperature = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date >= last_year).\
    order_by(Measurement.date).all()

    all_tobs = []
    for tobs in temperature:
        tobs_dict = {}
        tobs_dict["tobs"] = tobs
        all_tobs.append(tobs)

    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>")
def start(start):

    
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start"""

    start_query = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).group_by(Measurement.date).all()

    start_list = []
    for s in start_query:
        start_list.append(s)

    return jsonify(start_list)

    

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range"""
    
    start_end_query = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                    filter(Measurement.date >= start).filter(Measurement.date <= end).group_by(Measurement.date).all()

    start_end_list = []
    for se in start_end_query:
        start_end_list.append(se)

    return jsonify(start_end_list)



if __name__ == '__main__':
    app.run(debug=True)
