from datetime import datetime as dt, timedelta, timezone
from flask import Flask
import urllib.request
import json
import pandas as pd
from pprint import pprint
import config
#import matplotlib.pyplot as plt

app = Flask(__name__, static_folder="../build", static_url_path="/")

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/temp')
def get_current_time():

    #Get most recent timestamp for Hobolink
    curTime = (dt.now(timezone.utc) - timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S')
    prevTime = (dt.now(timezone.utc) - timedelta(minutes=20)).strftime('%Y-%m-%d %H:%M:%S')

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

    #RH North
    RHN12 = df.loc[df['sensor_sn'] == "20777735-2"]
    valueRHN = RHN12.iloc[0]['us_value']

    #RH South
    RHS12 = df.loc[df['sensor_sn'] == "20692768-2"]
    valueRHS = RHS12.iloc[0]['us_value']

    #Temperature soil North
    TSN = df.loc[df['sensor_sn'] == "20770089-1"]
    valueTSN = TSN.iloc[0]['us_value']

    #Temperature soil South
    TSS = df.loc[df['sensor_sn'] == "20684342-1"]
    valueTSS = TSS.iloc[0]['us_value']

    #Leaf Wetness North
    LWN = df.loc[df['sensor_sn'] == "20774075-1"]
    valueLWN = LWN.iloc[0]['us_value']

    #Leaf Wetness South
    LWS = df.loc[df['sensor_sn'] == "20650716-1"]
    valueLWS = LWS.iloc[0]['us_value']

    #Dew Point North
    DPN = df.loc[df['sensor_sn'] == "20777735-3"]
    valueDPN = DPN.iloc[0]['us_value']

    #Dew Point South
    DPS = df.loc[df['sensor_sn'] == "20692768-3"]
    valueDPS = DPS.iloc[0]['us_value'] 

    #Rain North
    RN = df.loc[df['sensor_sn'] == "20775973-1"]
    valueRN = RN.iloc[0]['us_value']

    #Rain South
    RS = df.loc[df['sensor_sn'] == "20696900-1"]
    valueRS = RS.iloc[0]['us_value'] 

    #Solar Radiation North
    SRN = df.loc[df['sensor_sn'] == "20779661-1"]
    valueSRN = SRN.iloc[0]['us_value']

    #Solar Radiation South
    SRS = df.loc[df['sensor_sn'] == "20683743-1"]
    valueSRS = SRS.iloc[0]['us_value'] 

    #Water Content Soil North
    WCSN = df.loc[df['sensor_sn'] == "20773509-1"]
    valueWCSN = WCSN.iloc[0]['us_value'] 

    #Water Content Soil North
    WCSS = df.loc[df['sensor_sn'] == "20696181-1"]
    valueWCSS = WCSS.iloc[0]['us_value'] 

    return {'tempN': "%.2f" % float(valueNA), 'tempS': "%.2f" % float(valueSA),
    'RHN': "%.2f" % float(valueRHN), 'RHS': "%.2f" % float(valueRHS),
    'TSN': "%.2f" % float(valueTSN), 'TSS': "%.2f" % float(valueTSS),
    'LWN': "%.2f" % float(valueLWN), 'LWS': "%.2f" % float(valueLWS),
    'DPN': "%.2f" % float(valueDPN), 'DPS': "%.2f" % float(valueDPS),
    'RN': "%.2f" % float(valueRN), 'RS': "%.2f" % float(valueRS),
    'SRN': "%.2f" % float(valueSRN), 'SRS': "%.2f" % float(valueSRS),
    'WCSN': "%.2f" % float(valueWCSN), 'WCSS': "%.2f" % float(valueWCSS),
    }
