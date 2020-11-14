import time
import datetime
from flask import Flask
import urllib.request
import json
import pandas as pd
from pprint import pprint
import config
from flask import render_template

app = Flask(__name__)

@app.route('/api/temp')
def get_current_time():

    #Get most recent timestamp for Hobolink
    curTime = (datetime.datetime.now() + datetime.timedelta(hours=5)- datetime.timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S')
    prevTime = (datetime.datetime.now() + datetime.timedelta(hours=5) - datetime.timedelta(minutes=20)).strftime('%Y-%m-%d %H:%M:%S')

    #Initialize parameters for API
    url = "https://webservice.hobolink.com/restv2/data/json"

    values = {
    "action": "",
    "authentication": {
        "password": config.password,
        "token": config.token,
        "user": config.username
    },
    "query": {
        "end_date_time": curTime,
        "loggers": [20777720,20699245,1],
        "start_date_time": prevTime
    }
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    #Get data
    data = json.dumps(values).encode("utf-8")

    try:
        req = urllib.request.Request(url, data, headers)
        with urllib.request.urlopen(req) as f:
            res = f.read()
    except Exception as e:
        pprint(e)

    #Convert response to a pandas dataframe
    data = json.loads(res.decode())
    df = pd.json_normalize(data['observationList'])

    #North air temperature
    rowNA = df.loc[df['sensor_sn'] == "20777735-1"]
    valueNA = rowNA.iloc[0]['us_value']

    #South air temperature
    rowSA = df.loc[df['sensor_sn'] == "20692768-1"]
    valueSA = rowSA.iloc[0]['us_value']

    return {'temp1': "%.2f" % float(valueNA), 'temp2': "%.2f" % float(valueSA)}

@app.route('/api/tempArray')
def get_temp_array():
    #Get last 12 hours of data
    curTime = (datetime.datetime.now() + datetime.timedelta(hours=5)- datetime.timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S')
    prevTime = (datetime.datetime.now() + datetime.timedelta(hours=5) - datetime.timedelta(minutes=15) - datetime.timedelta(hours=12)).strftime('%Y-%m-%d %H:%M:%S')

    #Specify values

    url = "https://webservice.hobolink.com/restv2/data/json"

    values = {
        "action": "",
        "authentication": {
        "password": config.password,
        "token": config.token,
        "user": config.username
    },
        "query": {
        "end_date_time": curTime,
        "loggers": [20777720,20699245,1],
        "start_date_time": prevTime
        }
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    #Get data

    data = json.dumps(values).encode("utf-8")
    #pprint(data)

    try:
        req = urllib.request.Request(url, data, headers)
        with urllib.request.urlopen(req) as f:
            res = f.read()
        #pprint(res.decode())
    except Exception as e:
        pprint(e)
    
    #Convert response to a pandas dataframe
    data = json.loads(res.decode())
    df = pd.json_normalize(data['observationList'])
    #df.to_csv("data.csv")

    #Temperature air North
    tempN12 = df.loc[df['sensor_sn'] == "20777735-1"]
    tempN12 = tempN12[['timestamp','us_value']]
    tempN12 = tempN12.rename(columns={"us_value": "North"})

    #Temperature air South
    tempS12 = df.loc[df['sensor_sn'] == "20692768-1"]
    tempS12 = tempS12[['timestamp','us_value']]
    tempS12 = tempS12.rename(columns={"us_value": "South"})

    return {'North': tempN12.to_json(), 'South': tempS12.to_json()} 

