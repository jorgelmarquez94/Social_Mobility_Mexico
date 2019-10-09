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

IMG_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///MMSI_2016.sqlite")


#################################################
# Flask Routes
#################################################
@app.route("/")
def homepage():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'undraw_all_the_data_h4ki.jpg')
    #Return the maps page.
    return render_template("index.html", image = full_filename)

@app.route("/map")
def map():
    #Return the maps page.
    return render_template("maps.html")

@app.route("/gender")
def gender():
    #Return the homepage.
    return render_template("gender.html")

@app.route("/gender/getMyVariables")
def variable_gender():
    results = engine.execute("SELECT DISTINCT Variable FROM MMSI_2016_Demográficos Where demografico = 'Sexo'")
    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    ##df = df.to_json(orient='columns')
    return jsonify(list(df.columns)[2:])

@app.route("/gender/getMyJson")
def getMyJsonGender():
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Sexo'")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df)

@app.route("/gender/<var>")
def sample_gender(var):
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Sexo' and variable = var")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df)

@app.route("/generation")
def generation():
    #Return the homepage.
    return render_template("generations.html")

@app.route("/generation/getMyVariables")
def variable_generation():
    results = engine.execute("SELECT DISTINCT Variable FROM MMSI_2016_Demográficos Where demografico = 'Generación'")
    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    ##df = df.to_json(orient='columns')
    return jsonify(list(df.columns)[2:])

@app.route("/generation/getMyJson")
def getMyJsonGeneration():
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Generación'")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df)

@app.route("/generation/<var>")
def sample_generation(var): 
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Generación' and variable = var")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df)

@app.route("/indigenous_languages")
def indigenous_languages():
    #Return the homepage.
    return render_template("indigenous_languages.html")

@app.route("/indigenous_languages/getMyVariables")
def variable_indigenous_languages():
    results = engine.execute("SELECT DISTINCT Variable FROM MMSI_2016_Demográficos Where demografico = 'Lengua_Indígena'")
    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    ##df = df.to_json(orient='columns')
    return jsonify(list(df.columns)[2:])

@app.route("/indigenous_languages/getMyJson")
def getMyJsonIndigenousLanguages():
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Lengua_Indígena'")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df)

@app.route("/indigenous_languages/<var>")
def sample_indigenous_languages(var): 
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Lengua_Indígena' and variable = var")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df) 

@app.route("/racial_origin")
def racial_origin():
    #Return the homepage.
    return render_template("racial_origin.html")

@app.route("/racial_origin/getMyVariables")
def variable_racial_origin():
    results = engine.execute("SELECT DISTINCT Variable FROM MMSI_2016_Demográficos Where demografico = 'Origen_Racial'")
    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    ##df = df.to_json(orient='columns')
    return jsonify(list(df.columns)[2:])

@app.route("/racial_origin/getMyJson")
def getMyJsonRacilOrigin():
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Origen_Racial'")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df)

@app.route("/racial_origin/<var>")
def sample_racial_origin(var): 
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Origen_Racial' and variable = var")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df)  

@app.route("/skin_color")
def skin_color():
    #Return the homepage.
    return render_template("skin_color.html")

@app.route("/skin_color/getMyVariables")
def variable_skin_color():
    results = engine.execute("SELECT DISTINCT Variable FROM MMSI_2016_Demográficos Where demografico = 'Color_Piel'")
    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    ##df = df.to_json(orient='columns')
    return jsonify(list(df.columns)[2:])

@app.route("/skin_color/getMyJson")
def getMyJsonSkinColor():
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Color_Piel'")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df)

@app.route("/skin_color/<var>")
def sample_skin_color(var): 
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Color_Piel' and variable = var")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df)       

@app.route("/socio_economic_background")
def socio_economic_background():
    #Return the homepage.
    return render_template("socio-economic_background.html")

@app.route("/socio_economic_background/getMyVariables")
def variable_socio_economic_background():
    results = engine.execute("SELECT DISTINCT Variable FROM MMSI_2016_Demográficos Where demografico = 'Estrato_Socioeconómico'")
    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    ##df = df.to_json(orient='columns')
    return jsonify(list(df.columns)[2:])

@app.route("/socio_economic_background/getMyJson")
def getMyJsonSocioEconomicBackground():
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Estrato_Socioeconómico'")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df)

@app.route("/socio_economic_background/<var>")
def sample_socio_economic_background(var):
    """Return a list of specific demographic data"""
    
    results = engine.execute("SELECT Variable,perspectiva_se_14_anios,opinion_situacion_economica,factor_expansion,Node_color,Link_color FROM MMSI_2016_Demográficos Where demografico = 'Estrato_Socioeconómico' and variable = var")

    # Create a dictionary entry for each row of metadata information
    df = DataFrame(results.fetchall())
    df.columns = results.keys()
    df = df.to_json(orient='columns')

    return(df)

if __name__ == '__main__':
    app.run(debug=True)
