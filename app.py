import os

import pandas as pd
from pandas import DataFrame
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///MMSI_2016.sqlite")


#################################################
# Flask Routes
#################################################

@app.route("/gender")
def index():
    #Return the homepage.
    return render_template("gender.html")


@app.route("/gender")
def load_json():
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,Perspectiva_SE_14_años,Opinión_Situación_Económica,Factor_Expansión,Node_color,Link_color FROM MMSI_2016_Demográficos Where Demográfico = 'Sexo'")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json()

    print(df)
    return jsonify(df)

@app.route("/map")
def map():
    #Return the maps page.
    return render_template("maps.html")

if __name__ == '__main__':
    app.run(debug=True)
