import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


#################################################
# Database Setup
#################################################
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///MMSI_2016.sqlite"
db = SQLAlchemy(app)
#engine = create_engine("sqlite:///MMSI_2016.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Demograficos = Base.classes.MMSI_2016_Demográficos

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all demograficos

    sel = [
        Demograficos.Variable,
        Demograficos.Factor_Expansión
    ]

    results = db.session.query(Demograficos.Variable,func.sum(Demograficos.Factor_Expansión).label('total')).filter(Demograficos.variable == 'Estrato_Socioeconómico').group_by(Demograficos.Variable).all()

    # Create a dictionary entry for each row of metadata information
    all_estratos = {}
    for result in results:
        Demograficos["Variable"] = result[0]
        Demograficos["Total"] = result[1]

    print(all_estratos)
    return jsonify(all_estratos)

@app.route("/map")
def map():
    #Return the maps page.
    return render_template("maps.html")

if __name__ == '__main__':
    app.run(debug=True)
