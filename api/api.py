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
    ATM = df.loc[df['sensor_sn'] == "20683649-1"]
    valueATM = ATM.iloc[0]['us_value']
    ATE = df.loc[df['sensor_sn'] == "20677838-1"]
    valueATE = ATE.iloc[0]['us_value']
    ATX = df.loc[df['sensor_sn'] == "20683651-1"]
    valueATX = ATX.iloc[0]['us_value']

    #South air temperature
    rowSA = df.loc[df['sensor_sn'] == "20692768-1"]
    valueSA = rowSA.iloc[0]['us_value']
    ATG = df.loc[df['sensor_sn'] == "20677839-1"]
    valueATG = ATG.iloc[0]['us_value']
    ATA16 = df.loc[df['sensor_sn'] == "20677837-1"]
    valueATA16 = ATA16.iloc[0]['us_value']
    ATY = df.loc[df['sensor_sn'] == "20683650-1"]
    valueATY = ATY.iloc[0]['us_value']
    ATA11 = df.loc[df['sensor_sn'] == "20677836-1"]
    valueATA11 = ATA11.iloc[0]['us_value']

    #RH North
    RHN12 = df.loc[df['sensor_sn'] == "20777735-2"]
    valueRHN = RHN12.iloc[0]['us_value']
    RHM = df.loc[df['sensor_sn'] == "20683649-2"]
    valueRHM = RHM.iloc[0]['us_value']
    RHE = df.loc[df['sensor_sn'] == "20677838-2"]
    valueRHE = RHE.iloc[0]['us_value']
    RHX = df.loc[df['sensor_sn'] == "20683651-2"]
    valueRHX = RHX.iloc[0]['us_value']

    #RH South
    RHS12 = df.loc[df['sensor_sn'] == "20692768-2"]
    valueRHS = RHS12.iloc[0]['us_value']
    RHG = df.loc[df['sensor_sn'] == "20677839-2"]
    valueRHG = RHG.iloc[0]['us_value']
    RHA16 = df.loc[df['sensor_sn'] == "20677837-2"]
    valueRHA16 = RHA16.iloc[0]['us_value']
    RHY = df.loc[df['sensor_sn'] == "20683650-2"]
    valueRHY = RHY.iloc[0]['us_value']
    RHA11 = df.loc[df['sensor_sn'] == "20677836-2"]
    valueRHA11 = RHA11.iloc[0]['us_value']

    #Dew Point North
    DPN = df.loc[df['sensor_sn'] == "20777735-3"]
    valueDPN = DPN.iloc[0]['us_value']
    DPM = df.loc[df['sensor_sn'] == "20683649-3"]
    valueDPM = DPM.iloc[0]['us_value']
    DPE = df.loc[df['sensor_sn'] == "20677838-3"]
    valueDPE = DPE.iloc[0]['us_value']
    DPX = df.loc[df['sensor_sn'] == "20683651-3"]
    valueDPX = DPX.iloc[0]['us_value']

    #Dew Point South
    DPS = df.loc[df['sensor_sn'] == "20692768-3"]
    valueDPS = DPS.iloc[0]['us_value'] 
    DPG = df.loc[df['sensor_sn'] == "20677839-3"]
    valueDPG = DPG.iloc[0]['us_value']
    DPA16 = df.loc[df['sensor_sn'] == "20677837-3"]
    valueDPA16 = DPA16.iloc[0]['us_value']
    DPY = df.loc[df['sensor_sn'] == "20683650-3"]
    valueDPY = DPY.iloc[0]['us_value']
    DPA11 = df.loc[df['sensor_sn'] == "20677836-3"]
    valueDPA11 = DPA11.iloc[0]['us_value']

    #Temperature soil North
    TSN = df.loc[df['sensor_sn'] == "20770089-1"]
    valueTSN = TSN.iloc[0]['us_value']
    TSM = df.loc[df['sensor_sn'] == "20683693-1"]
    valueTSM = TSM.iloc[0]['us_value']
    TSE = df.loc[df['sensor_sn'] == "20683722-1"]
    valueTSE = TSE.iloc[0]['us_value']
    TSX = df.loc[df['sensor_sn'] == "20683695-1"]
    valueTSX = TSX.iloc[0]['us_value']

    #Temperature soil South
    TSS = df.loc[df['sensor_sn'] == "20684342-1"]
    valueTSS = TSS.iloc[0]['us_value']
    TSG = df.loc[df['sensor_sn'] == "20683697-1"]
    valueTSG = TSG.iloc[0]['us_value']
    TSA16 = df.loc[df['sensor_sn'] == "20683696-1"]
    valueTSA16 = TSA16.iloc[0]['us_value']
    TSY = df.loc[df['sensor_sn'] == "20683694-1"]
    valueTSY = TSY.iloc[0]['us_value']
    TSA11 = df.loc[df['sensor_sn'] == "20683723-1"]
    valueTSA11 = TSA11.iloc[0]['us_value']

    #Leaf Wetness North
    LWN = df.loc[df['sensor_sn'] == "20774075-1"]
    valueLWN = LWN.iloc[0]['us_value']
    LWM = df.loc[df['sensor_sn'] == "20776878-1"]
    valueLWM = LWM.iloc[0]['us_value']
    LWE = df.loc[df['sensor_sn'] == "20778340-1"]
    valueLWE = LWE.iloc[0]['us_value']
    LWX = df.loc[df['sensor_sn'] == "20780842-1"]
    valueLWX = LWX.iloc[0]['us_value']

    #Leaf Wetness South
    LWS = df.loc[df['sensor_sn'] == "20650716-1"]
    valueLWS = LWS.iloc[0]['us_value']
    LWG = df.loc[df['sensor_sn'] == "20778341-1"]
    valueLWG = LWG.iloc[0]['us_value']
    LWA16 = df.loc[df['sensor_sn'] == "20776877-1"]
    valueLWA16 = LWA16.iloc[0]['us_value']
    LWY = df.loc[df['sensor_sn'] == "20778339-1"]
    valueLWY = LWY.iloc[0]['us_value']
    LWA11 = df.loc[df['sensor_sn'] == "20778342-1"]
    valueLWA11 = LWA11.iloc[0]['us_value']

    #Rain North
    RN = df.loc[df['sensor_sn'] == "20775973-1"]
    valueRN = RN.iloc[0]['us_value']
    RM = df.loc[df['sensor_sn'] == "20683599-1"]
    valueRM = RM.iloc[0]['us_value']
    RE = df.loc[df['sensor_sn'] == "20683600-1"]
    valueRE = RE.iloc[0]['us_value']
    RX = df.loc[df['sensor_sn'] == "20629502-1"]
    valueRX = RX.iloc[0]['us_value']

    #Rain South
    RS = df.loc[df['sensor_sn'] == "20696900-1"]
    valueRS = RS.iloc[0]['us_value'] 
    RG = df.loc[df['sensor_sn'] == "20810982-1"]
    valueRG = RG.iloc[0]['us_value']
    RA16 = df.loc[df['sensor_sn'] == "20683603-1"]
    valueRA16 = RA16.iloc[0]['us_value']
    RY = df.loc[df['sensor_sn'] == "20683602-1"]
    valueRY = RY.iloc[0]['us_value']
    RA11 = df.loc[df['sensor_sn'] == "20683601-1"]
    valueRA11 = RA11.iloc[0]['us_value']

    #Solar Radiation North
    SRN = df.loc[df['sensor_sn'] == "20779661-1"]
    valueSRN = SRN.iloc[0]['us_value']
    SRM = df.loc[df['sensor_sn'] == "20864948-1"]
    valueSRM = SRM.iloc[0]['us_value']
    SRE = df.loc[df['sensor_sn'] == "20413294-1"]
    valueSRE = SRE.iloc[0]['us_value']
    SRX = df.loc[df['sensor_sn'] == "20735859-1"]
    valueSRX = SRX.iloc[0]['us_value']

    #Solar Radiation South
    SRS = df.loc[df['sensor_sn'] == "20683743-1"]
    valueSRS = SRS.iloc[0]['us_value'] 
    SRG = df.loc[df['sensor_sn'] == "20413291-1"]
    valueSRG = SRG.iloc[0]['us_value']
    SRA16 = df.loc[df['sensor_sn'] == "20413293-1"]
    valueSRA16 = SRA16.iloc[0]['us_value']
    SRY = df.loc[df['sensor_sn'] == "20454637-1"]
    valueSRY = SRY.iloc[0]['us_value']
    SRA11 = df.loc[df['sensor_sn'] == "20413295-1"]
    valueSRA11 = SRA11.iloc[0]['us_value']

    #Water Content Soil North
    WCSN = df.loc[df['sensor_sn'] == "20773509-1"]
    valueWCSN = WCSN.iloc[0]['us_value'] 
    WCM = df.loc[df['sensor_sn'] == "20683612-1"]
    valueWCM = WCM.iloc[0]['us_value']
    WCE = df.loc[df['sensor_sn'] == "20683614-1"]
    valueWCE = WCE.iloc[0]['us_value']
    WCX = df.loc[df['sensor_sn'] == "20683610-1"]
    valueWCX = WCX.iloc[0]['us_value']

    #Water Content Soil South
    WCSS = df.loc[df['sensor_sn'] == "20696181-1"]
    valueWCSS = WCSS.iloc[0]['us_value']
    WCG = df.loc[df['sensor_sn'] == "20683611-1"]
    valueWCG = WCG.iloc[0]['us_value']
    WCA16 = df.loc[df['sensor_sn'] == "20543770-1"]
    valueWCA16 = WCA16.iloc[0]['us_value']
    WCY = df.loc[df['sensor_sn'] == "20683615-1"]
    valueWCY = WCY.iloc[0]['us_value']
    WCA11 = df.loc[df['sensor_sn'] == "20683609-1"]
    valueWCA11 = WCA11.iloc[0]['us_value'] 

    #Wind Speeds North
    WSN = df.loc[df['sensor_sn'] == "20772423-1"]
    valueWSN = WSN.iloc[0]['us_value']
    WSM = df.loc[df['sensor_sn'] == "20696852-1"]
    valueWSM = WSM.iloc[0]['us_value']
    WSE = df.loc[df['sensor_sn'] == "20657340-1"]
    valueWSE = WSE.iloc[0]['us_value']
    WSX = df.loc[df['sensor_sn'] == "20696851-1"]
    valueWSX = WSX.iloc[0]['us_value']

    #Wind Speeds South
    WSS = df.loc[df['sensor_sn'] == "20673566-1"]
    valueWSS = WSS.iloc[0]['us_value']
    WSG = df.loc[df['sensor_sn'] == "20657341-1"]
    valueWSG = WSG.iloc[0]['us_value']
    WSA16 = df.loc[df['sensor_sn'] == "20696853-1"]
    valueWSA16 = WSA16.iloc[0]['us_value']
    WSY = df.loc[df['sensor_sn'] == "20851758-1"]
    valueWSY = WSY.iloc[0]['us_value']
    WSA11 = df.loc[df['sensor_sn'] == "20696855-1"]
    valueWSA11 = WSA11.iloc[0]['us_value']

    #Gust Speeds North
    GSN = df.loc[df['sensor_sn'] == "20772423-2"]
    valueGSN = GSN.iloc[0]['us_value']
    GSM = df.loc[df['sensor_sn'] == "20696852-2"]
    valueGSM = GSM.iloc[0]['us_value']
    GSE = df.loc[df['sensor_sn'] == "20657340-2"]
    valueGSE = GSE.iloc[0]['us_value']
    GSX = df.loc[df['sensor_sn'] == "20696851-2"]
    valueGSX = GSX.iloc[0]['us_value']

    #Gust Speeds South
    GSS = df.loc[df['sensor_sn'] == "20673566-2"]
    valueGSS = GSS.iloc[0]['us_value']
    GSG = df.loc[df['sensor_sn'] == "20657341-2"]
    valueGSG = GSG.iloc[0]['us_value']
    GSA16 = df.loc[df['sensor_sn'] == "20696853-2"]
    valueGSA16 = GSA16.iloc[0]['us_value']
    GSY = df.loc[df['sensor_sn'] == "20851758-2"]
    valueGSY = GSY.iloc[0]['us_value']
    GSA11 = df.loc[df['sensor_sn'] == "20696855-2"]
    valueGSA11 = GSA11.iloc[0]['us_value']

    #Wind Direction North (don't round)
    WDN = df.loc[df['sensor_sn'] == "20774012-1"]
    valueWDN = WDN.iloc[0]['us_value']
    WDM = df.loc[df['sensor_sn'] == "20696852-3"]
    valueWDM = WDM.iloc[0]['us_value']
    WDE = df.loc[df['sensor_sn'] == "20657340-3"]
    valueWDE = WDE.iloc[0]['us_value']
    WDX = df.loc[df['sensor_sn'] == "20696851-3"]
    valueWDX = WDX.iloc[0]['us_value']

    #Wind Direction South (don't round)
    WDS = df.loc[df['sensor_sn'] == "20677657-1"]
    valueWDS = WDS.iloc[0]['us_value']
    WDG = df.loc[df['sensor_sn'] == "20657341-3"]
    valueWDG = WDG.iloc[0]['us_value']
    WDA16 = df.loc[df['sensor_sn'] == "20696853-3"]
    valueWDA16 = WDA16.iloc[0]['us_value']
    WDY = df.loc[df['sensor_sn'] == "20851758-3"]
    valueWDY = WDY.iloc[0]['us_value']
    WDA11 = df.loc[df['sensor_sn'] == "20696855-3"]
    valueWDA11 = WDA11.iloc[0]['us_value']

    return {'tempN': "%.2f" % float(valueNA), 'tempS': "%.2f" % float(valueSA),
    'RHN': "%.2f" % float(valueRHN), 'RHS': "%.2f" % float(valueRHS),
    'TSN': "%.2f" % float(valueTSN), 'TSS': "%.2f" % float(valueTSS),
    'LWN': "%.2f" % float(valueLWN), 'LWS': "%.2f" % float(valueLWS),
    'DPN': "%.2f" % float(valueDPN), 'DPS': "%.2f" % float(valueDPS),
    'RN': "%.2f" % float(valueRN), 'RS': "%.2f" % float(valueRS),
    'SRN': "%.2f" % float(valueSRN), 'SRS': "%.2f" % float(valueSRS),
    'WCSN': "%.2f" % float(valueWCSN), 'WCSS': "%.2f" % float(valueWCSS),
    'ATM': "%.2f" % float(valueATM), 'ATE': "%.2f" % float(valueATE), 'ATX': "%.2f" % float(valueATX),
    'ATG': "%.2f" % float(valueATG), 'ATA16': "%.2f" % float(valueATA16), 'ATY': "%.2f" % float(valueATY), 'ATA11': "%.2f" % float(valueATA11),
    'RHM': "%.2f" % float(valueRHM), 'RHE': "%.2f" % float(valueRHE), 'RHX': "%.2f" % float(valueRHX),
    'RHG': "%.2f" % float(valueRHG), 'RHA16': "%.2f" % float(valueRHA16), 'RHY': "%.2f" % float(valueRHY), 'RHA11': "%.2f" % float(valueRHA11),
    'DPM': "%.2f" % float(valueDPM), 'DPE': "%.2f" % float(valueDPE), 'DPX': "%.2f" % float(valueDPX),
    'DPG': "%.2f" % float(valueDPG), 'DPA16': "%.2f" % float(valueDPA16), 'DPY': "%.2f" % float(valueDPY), 'DPA11': "%.2f" % float(valueDPA11),
    'TSM': "%.2f" % float(valueTSM), 'TSE': "%.2f" % float(valueTSE), 'TSX': "%.2f" % float(valueTSX),
    'TSG': "%.2f" % float(valueTSG), 'TSA16': "%.2f" % float(valueTSA16), 'TSY': "%.2f" % float(valueTSY), 'TSA11': "%.2f" % float(valueTSA11),
    'LWM': "%.2f" % float(valueLWM), 'LWE': "%.2f" % float(valueLWE), 'LWX': "%.2f" % float(valueLWX),
    'LWG': "%.2f" % float(valueLWG), 'LWA16': "%.2f" % float(valueLWA16), 'LWY': "%.2f" % float(valueLWY), 'LWA11': "%.2f" % float(valueLWA11),
    'RM': "%.2f" % float(valueRM), 'RE': "%.2f" % float(valueRE), 'RX': "%.2f" % float(valueRX),
    'RG': "%.2f" % float(valueRG), 'RA16': "%.2f" % float(valueRA16), 'RY': "%.2f" % float(valueRY), 'RA11': "%.2f" % float(valueRA11),
    'SRM': "%.2f" % float(valueSRM), 'SRE': "%.2f" % float(valueSRE), 'SRX': "%.2f" % float(valueSRX),
    'SRG': "%.2f" % float(valueSRG), 'SRA16': "%.2f" % float(valueSRA16), 'SRY': "%.2f" % float(valueSRY), 'SRA11': "%.2f" % float(valueSRA11),
    'WCM': "%.2f" % float(valueWCM), 'WCE': "%.2f" % float(valueWCE), 'WCX': "%.2f" % float(valueWCX),
    'WCG': "%.2f" % float(valueWCG), 'WCA16': "%.2f" % float(valueWCA16), 'WCY': "%.2f" % float(valueWCY), 'WCA11': "%.2f" % float(valueWCA11),
    'WSN': "%.2f" % float(valueWSN), 'WSM': "%.2f" % float(valueWSM), 'WSE': "%.2f" % float(valueWSE), 'WSX': "%.2f" % float(valueWSX),
    'WSS': "%.2f" % float(valueWSS),'WSG': "%.2f" % float(valueWSG), 'WSA16': "%.2f" % float(valueWSA16), 'WSY': "%.2f" % float(valueWSY), 'WSA11': "%.2f" % float(valueWSA11),
    'GSN': "%.2f" % float(valueGSN), 'GSM': "%.2f" % float(valueGSM), 'GSE': "%.2f" % float(valueGSE), 'GSX': "%.2f" % float(valueGSX),
    'GSS': "%.2f" % float(valueGSS),'GSG': "%.2f" % float(valueGSG), 'GSA16': "%.2f" % float(valueGSA16), 'GSY': "%.2f" % float(valueGSY), 'GSA11': "%.2f" % float(valueGSA11),
    'WDN': "%.2f" % float(valueWDN), 'WDM': "%.2f" % float(valueWDM), 'WDE': "%.2f" % float(valueWDE), 'WDX': "%.2f" % float(valueWDX),
    'WDS': "%.2f" % float(valueWDS), 'WDG':"%.2f" % float(valueWDG), 'WDA16': "%.2f" % float(valueWDA16), 'WDY':"%.2f" % float(valueWDY), 'WDA11': "%.2f" % float(valueWDA11),
    'time': curTime
    }
