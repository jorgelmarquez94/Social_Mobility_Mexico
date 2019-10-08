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
@app.route("/getMyJson")
def getMyJson():
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Sexo'")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df)

@app.route("/")
def homepage():
    #Return the maps page.
    return render_template("index.html")

@app.route("/map")
def map():
    #Return the maps page.
    return render_template("maps.html")

@app.route("/gender")
def gender():
    #Return the homepage.
    return render_template("gender.html")

@app.route("/gender/getMyJson")
def getMyJsonGender():
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Sexo'")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df)    

@app.route("/generation")
def generation():
    #Return the homepage.
    return render_template("generations.html")

@app.route("/generation/getMyJson")
def getMyJsonGeneration():
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Generación'")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df) 

@app.route("/indigenous_languages")
def indigenous_languages():
    #Return the homepage.
    return render_template("indigenous_languages.html")

@app.route("/indigenous_languages/getMyJson")
def getMyJsonIndigenousLanguages():
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Lengua_Indígena'")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df) 

@app.route("/racial_origin")
def racial_origin():
    #Return the homepage.
    return render_template("racial_origin.html")

@app.route("/racial_origin/getMyJson")
def getMyJsonRacilOrigin():
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Origen_Racial'")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df) 

@app.route("/skin_color")
def skin_color():
    #Return the homepage.
    return render_template("skin_color.html")

@app.route("/skin_color/getMyJson")
def getMyJsonSkinColor():
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Color_Piel'")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df) 

@app.route("/socio_economic_background")
def socio_economic_background():
    #Return the homepage.
    return render_template("socio-economic_background.html")

@app.route("/socio_economic_background/getMyJson")
def getMyJsonSocioEconomicBackground():
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Estrato_Socioeconómico'")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df)

if __name__ == '__main__':
    app.run(debug=True)
