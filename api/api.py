from datetime import datetime as dt, timedelta, timezone
from flask import Flask, request, Response
from api import app, db
from api.models import Scab
import urllib.request
import json
import pandas as pd
import numpy as np
from pprint import pprint
import pytz
import sys
import time

abstime = time.time()

#              N             M            E             X             S             G             A16           Y             A11        B3b
sensors = {
    "1": ["20777735-1", "20683649-1", "20677838-1", "20683651-1", "20692768-1", "20677839-1", "20677837-1", "20683650-1", "20677836-1"], #Air temperature
    "2": ["20777735-2", "20683649-2", "20677838-2", "20683651-2", "20692768-2", "20677839-2", "20677837-2", "20683650-2", "20677836-2"], # Rel humidity
    "3": ["20777735-3", "20683649-3", "20677838-3", "20683651-3", "20692768-3", "20677839-3", "20677837-3", "20683650-3", "20677836-3"], # Dew point
    "4": ["20775973-1", "20683599-1", "20683600-1", "20629502-1", "20696900-1", "20810982-1", "20683603-1", "20683602-1", "20683601-1"], # Rainfall
    "5": ["20774075-1", "20776878-1", "20778340-1", "20780842-1", "20650716-1", "20778341-1", "20776877-1", "20778339-1", "20778342-1", "20780849-1"], # Leaf wetness
    "6": ["20779661-1", "20864948-1", "20413294-1", "20735859-1", "20683743-1", "20413291-1", "20413293-1", "20454637-1", "20413295-1"], # Solar radiation
    "7": ["20770089-1", "20683693-1", "20683722-1", "20683695-1", "20684342-1", "20683697-1", "20683696-1", "20683694-1", "20683723-1"], # Soil temp
    "8": ["20773509-1", "20683612-1", "20683614-1", "20683610-1", "20696181-1", "20683611-1", "20543770-1", "20683615-1", "20683609-1"]  # Water content
}

def getscab():
    global abstime
    print("Abs time at scab start %d"%(time.time()-abstime))
    t = time.time()
    curTime = (dt.now(timezone.utc) - timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S')
    prevTime = (dt.now(timezone.utc) - timedelta(minutes=15) - timedelta(hours=41)).strftime('%Y-%m-%d %H:%M:%S') #Last 41 hours

    #Specify values

    url = "https://webservice.hobolink.com/restv2/data/json"

    values = {
    "action": "",
    "authentication": {
        "password": app.config['PASSWORD'],
        "token": app.config['TOKEN'],
        "user": app.config['USERNAME']
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
    print("Got scab data at %d seconds"%(time.time()-t))

    try:
        req = urllib.request.Request(url, data, headers)
        with urllib.request.urlopen(req) as f:
            res = f.read()
        data = json.loads(res.decode())
        df = pd.json_normalize(data['observationList']) 

        AvgT = 0
        t1 = time.time()
        print("Starting scab calc at %d"%(t1-abstime))
        #North
        if "20775973-1" in df.values and "20774075-1" in df.values and  df.loc[df['sensor_sn'] == "20775973-1"].iloc[-1]['us_value']>0.0: #check if rain & leaf wetness values exist and if it the latest rain value is > 0
            Count = sum(df.loc[df['sensor_sn'] == "20774075-1"]['us_value'][::-1].expanding().apply(lambda x: np.all(x>60))) #count no of hours it's been more than 60% wetness
            Hours = Count/12
            AvgT = df.loc[df['sensor_sn'] == "20777735-1"]['us_value'].tail(Count).mean() #get avg of temp value 
            if((AvgT >= 79 and Hours >= 11) or (AvgT >= 77 and Hours >= 8) or (AvgT >= 61 and Hours >= 6) or (AvgT >= 57 and Hours >= 7) or #apple scab logic
            (AvgT >= 54 and Hours >= 8) or (AvgT >= 52 and Hours >= 9) or (AvgT >= 50 and Hours >= 11) or (AvgT >= 48 and Hours >= 12) or
            (AvgT >= 46 and Hours >= 13) or (AvgT >= 45 and Hours >= 15) or (AvgT >= 43 and Hours >= 18) or (AvgT >= 41 and Hours >= 21) or
            (AvgT >= 39 and Hours >= 28) or (AvgT >= 37 and Hours >= 30) or (AvgT >= 36 and Hours >= 35) or (AvgT >= 34 and Hours >= 41)):
                ScLWN = "Yes"
            else:
                ScLWN = "No"   
        else:
            ScLWN = "No"
        print("Finished North at %d seconds"%(time.time()-t1))

        #M
        if "20683599-1" in df.values and "20776878-1" in df.values and  df.loc[df['sensor_sn'] == "20683599-1"].iloc[-1]['us_value']>0.0: #check if rain & leaf wetness values exist and if it the latest rain value is > 0
            Count = sum(df.loc[df['sensor_sn'] == "20776878-1"]['us_value'][::-1].expanding().apply(lambda x: np.all(x>60))) #count no of hours it's been more than 60% wetness
            Hours = Count/12
            AvgT = df.loc[df['sensor_sn'] == "20683649-1"]['us_value'].tail(Count).mean() #get avg of temp value
            if((AvgT >= 79 and Hours >= 11) or (AvgT >= 77 and Hours >= 8) or (AvgT >= 61 and Hours >= 6) or (AvgT >= 57 and Hours >= 7) or #apple scab logic
            (AvgT >= 54 and Hours >= 8) or (AvgT >= 52 and Hours >= 9) or (AvgT >= 50 and Hours >= 11) or (AvgT >= 48 and Hours >= 12) or
            (AvgT >= 46 and Hours >= 13) or (AvgT >= 45 and Hours >= 15) or (AvgT >= 43 and Hours >= 18) or (AvgT >= 41 and Hours >= 21) or
            (AvgT >= 39 and Hours >= 28) or (AvgT >= 37 and Hours >= 30) or (AvgT >= 36 and Hours >= 35) or (AvgT >= 34 and Hours >= 41)):
                ScLWM = "Yes"
            else:
                ScLWM = "No"   
        else:
            ScLWM = "No" 
        print("Finished M at %d seconds"%(time.time()-t1))

        #E
        if "20683600-1" in df.values and "20778340-1" in df.values and  df.loc[df['sensor_sn'] == "20683600-1"].iloc[-1]['us_value']>0.0: #check if rain & leaf wetness values exist and if it the latest rain value is > 0
            Count = sum(df.loc[df['sensor_sn'] == "20778340-1"]['us_value'][::-1].expanding().apply(lambda x: np.all(x>60))) #count no of hours it's been more than 60% wetness
            Hours = Count/12
            AvgT = df.loc[df['sensor_sn'] == "20677838-1"]['us_value'].tail(Count).mean() #get avg of temp value
            if((AvgT >= 79 and Hours >= 11) or (AvgT >= 77 and Hours >= 8) or (AvgT >= 61 and Hours >= 6) or (AvgT >= 57 and Hours >= 7) or #apple scab logic
            (AvgT >= 54 and Hours >= 8) or (AvgT >= 52 and Hours >= 9) or (AvgT >= 50 and Hours >= 11) or (AvgT >= 48 and Hours >= 12) or
            (AvgT >= 46 and Hours >= 13) or (AvgT >= 45 and Hours >= 15) or (AvgT >= 43 and Hours >= 18) or (AvgT >= 41 and Hours >= 21) or
            (AvgT >= 39 and Hours >= 28) or (AvgT >= 37 and Hours >= 30) or (AvgT >= 36 and Hours >= 35) or (AvgT >= 34 and Hours >= 41)):
                ScLWE = "Yes"
            else:
                ScLWE = "No"   
        else:
            ScLWE = "No"     
        print("Finished E at %d seconds"%(time.time()-t1))

        #X
        if "20629502-1" in df.values and "20780842-1" in df.values and  df.loc[df['sensor_sn'] == "20629502-1"].iloc[-1]['us_value']>0.0: #check if rain & leaf wetness values exist and if it the latest rain value is > 0
            Count = sum(df.loc[df['sensor_sn'] == "20780842-1"]['us_value'][::-1].expanding().apply(lambda x: np.all(x>60))) #count no of hours it's been more than 60% wetness
            Hours = Count/12
            AvgT = df.loc[df['sensor_sn'] == "20683651-1"]['us_value'].tail(Count).mean() #get avg of temp value
            if((AvgT >= 79 and Hours >= 11) or (AvgT >= 77 and Hours >= 8) or (AvgT >= 61 and Hours >= 6) or (AvgT >= 57 and Hours >= 7) or #apple scab logic
            (AvgT >= 54 and Hours >= 8) or (AvgT >= 52 and Hours >= 9) or (AvgT >= 50 and Hours >= 11) or (AvgT >= 48 and Hours >= 12) or
            (AvgT >= 46 and Hours >= 13) or (AvgT >= 45 and Hours >= 15) or (AvgT >= 43 and Hours >= 18) or (AvgT >= 41 and Hours >= 21) or
            (AvgT >= 39 and Hours >= 28) or (AvgT >= 37 and Hours >= 30) or (AvgT >= 36 and Hours >= 35) or (AvgT >= 34 and Hours >= 41)):
                ScLWX = "Yes"
            else:
                ScLWX = "No"   
        else:
            ScLWX = "No" 
        print("Finished X at %d seconds"%(time.time()-t1))

        #Leaf Wetness South
        if "20696900-1" in df.values and "20650716-1" in df.values and  df.loc[df['sensor_sn'] == "20696900-1"].iloc[-1]['us_value']>0.0: #check if rain & leaf wetness values exist and if it the latest rain value is > 0
            Count = sum(df.loc[df['sensor_sn'] == "20650716-1"]['us_value'][::-1].expanding().apply(lambda x: np.all(x>60))) #count no of hours it's been more than 60% wetness
            Hours = Count/12
            AvgT = df.loc[df['sensor_sn'] == "20692768-1"]['us_value'].tail(Count).mean() #get avg of temp value
            if((AvgT >= 79 and Hours >= 11) or (AvgT >= 77 and Hours >= 8) or (AvgT >= 61 and Hours >= 6) or (AvgT >= 57 and Hours >= 7) or #apple scab logic
            (AvgT >= 54 and Hours >= 8) or (AvgT >= 52 and Hours >= 9) or (AvgT >= 50 and Hours >= 11) or (AvgT >= 48 and Hours >= 12) or
            (AvgT >= 46 and Hours >= 13) or (AvgT >= 45 and Hours >= 15) or (AvgT >= 43 and Hours >= 18) or (AvgT >= 41 and Hours >= 21) or
            (AvgT >= 39 and Hours >= 28) or (AvgT >= 37 and Hours >= 30) or (AvgT >= 36 and Hours >= 35) or (AvgT >= 34 and Hours >= 41)):
                ScLWS = "Yes"
            else:
                ScLWS = "No"   
        else:
            ScLWS = "No" 
        print("Finished S at %d seconds"%(time.time()-t1))

        #G
        if "20810982-1" in df.values and "20778341-1" in df.values and  df.loc[df['sensor_sn'] == "20810982-1"].iloc[-1]['us_value']>0.0: #check if rain & leaf wetness values exist and if it the latest rain value is > 0
            Count = sum(df.loc[df['sensor_sn'] == "20778341-1"]['us_value'][::-1].expanding().apply(lambda x: np.all(x>60))) #count no of hours it's been more than 60% wetness
            Hours = Count/12
            AvgT = df.loc[df['sensor_sn'] == "20677839-1"]['us_value'].tail(Count).mean() #get avg of temp value
            if((AvgT >= 79 and Hours >= 11) or (AvgT >= 77 and Hours >= 8) or (AvgT >= 61 and Hours >= 6) or (AvgT >= 57 and Hours >= 7) or #apple scab logic
            (AvgT >= 54 and Hours >= 8) or (AvgT >= 52 and Hours >= 9) or (AvgT >= 50 and Hours >= 11) or (AvgT >= 48 and Hours >= 12) or
            (AvgT >= 46 and Hours >= 13) or (AvgT >= 45 and Hours >= 15) or (AvgT >= 43 and Hours >= 18) or (AvgT >= 41 and Hours >= 21) or
            (AvgT >= 39 and Hours >= 28) or (AvgT >= 37 and Hours >= 30) or (AvgT >= 36 and Hours >= 35) or (AvgT >= 34 and Hours >= 41)):
                ScLWG = "Yes"
            else:
                ScLWG = "No"   
        else:
            ScLWG = "No" 
        print("Finished G at %d seconds"%(time.time()-t1))

        #A16
        if "20683603-1" in df.values and "20776877-1" in df.values and  df.loc[df['sensor_sn'] == "20683603-1"].iloc[-1]['us_value']>0.0: #check if rain & leaf wetness values exist and if it the latest rain value is > 0
            Count = sum(df.loc[df['sensor_sn'] == "20776877-1"]['us_value'][::-1].expanding().apply(lambda x: np.all(x>60))) #count no of hours it's been more than 60% wetness
            Hours = Count/12
            AvgT = df.loc[df['sensor_sn'] == "20677837-1"]['us_value'].tail(Count).mean() #get avg of temp value
            if((AvgT >= 79 and Hours >= 11) or (AvgT >= 77 and Hours >= 8) or (AvgT >= 61 and Hours >= 6) or (AvgT >= 57 and Hours >= 7) or #apple scab logic
            (AvgT >= 54 and Hours >= 8) or (AvgT >= 52 and Hours >= 9) or (AvgT >= 50 and Hours >= 11) or (AvgT >= 48 and Hours >= 12) or
            (AvgT >= 46 and Hours >= 13) or (AvgT >= 45 and Hours >= 15) or (AvgT >= 43 and Hours >= 18) or (AvgT >= 41 and Hours >= 21) or
            (AvgT >= 39 and Hours >= 28) or (AvgT >= 37 and Hours >= 30) or (AvgT >= 36 and Hours >= 35) or (AvgT >= 34 and Hours >= 41)):
                ScLWA16 = "Yes"
            else:
                ScLWA16 = "No"   
        else:
            ScLWA16 = "No"  
        print("Finished A16 at %d seconds"%(time.time()-t1))

        #Y
        if "20683602-1" in df.values and "20778339-1" in df.values and  df.loc[df['sensor_sn'] == "20683602-1"].iloc[-1]['us_value']>0.0: #check if rain & leaf wetness values exist and if it the latest rain value is > 0
            Count = sum(df.loc[df['sensor_sn'] == "20778339-1"]['us_value'][::-1].expanding().apply(lambda x: np.all(x>60))) #count no of hours it's been more than 60% wetness
            Hours = Count/12
            AvgT = df.loc[df['sensor_sn'] == "20683650-1"]['us_value'].tail(Count).mean() #get avg of temp value
            if((AvgT >= 79 and Hours >= 11) or (AvgT >= 77 and Hours >= 8) or (AvgT >= 61 and Hours >= 6) or (AvgT >= 57 and Hours >= 7) or #apple scab logic
            (AvgT >= 54 and Hours >= 8) or (AvgT >= 52 and Hours >= 9) or (AvgT >= 50 and Hours >= 11) or (AvgT >= 48 and Hours >= 12) or
            (AvgT >= 46 and Hours >= 13) or (AvgT >= 45 and Hours >= 15) or (AvgT >= 43 and Hours >= 18) or (AvgT >= 41 and Hours >= 21) or
            (AvgT >= 39 and Hours >= 28) or (AvgT >= 37 and Hours >= 30) or (AvgT >= 36 and Hours >= 35) or (AvgT >= 34 and Hours >= 41)):
                ScLWY = "Yes"
            else:
                ScLWY = "No"   
        else:
            ScLWY = "No" 
        print("Finished Y at %d seconds"%(time.time()-t1)) 

        #A11
        if "20683601-1" in df.values and "20778342-1" in df.values and  df.loc[df['sensor_sn'] == "20683601-1"].iloc[-1]['us_value']>0.0: #check if rain & leaf wetness values exist and if it the latest rain value is > 0
            Count = sum(df.loc[df['sensor_sn'] == "20778342-1"]['us_value'][::-1].expanding().apply(lambda x: np.all(x>60))) #count no of hours it's been more than 60% wetness
            Hours = Count/12
            AvgT = df.loc[df['sensor_sn'] == "20677836-1"]['us_value'].tail(Count).mean() #get avg of temp value
            if((AvgT >= 79 and Hours >= 11) or (AvgT >= 77 and Hours >= 8) or (AvgT >= 61 and Hours >= 6) or (AvgT >= 57 and Hours >= 7) or #apple scab logic
            (AvgT >= 54 and Hours >= 8) or (AvgT >= 52 and Hours >= 9) or (AvgT >= 50 and Hours >= 11) or (AvgT >= 48 and Hours >= 12) or
            (AvgT >= 46 and Hours >= 13) or (AvgT >= 45 and Hours >= 15) or (AvgT >= 43 and Hours >= 18) or (AvgT >= 41 and Hours >= 21) or
            (AvgT >= 39 and Hours >= 28) or (AvgT >= 37 and Hours >= 30) or (AvgT >= 36 and Hours >= 35) or (AvgT >= 34 and Hours >= 41)):
                ScLWA11 = "Yes"
            else:
                ScLWA11 = "No"   
        else:
            ScLWA11 = "No" 
        
        print("Finishing scab api at %d seconds"%(time.time()-t))
        
        # Write scab warnings to database
        existingEntry = Scab.query.filter_by(timestamp=dt.now(timezone.utc).date()).first()
        if existingEntry is None and (ScLWN == "Yes" or ScLWM == "Yes" or ScLWE == "Yes" or ScLWX == "Yes" or 
        ScLWS == "Yes" or ScLWG == "Yes" or ScLWA16 == "Yes" or ScLWY == "Yes" or ScLWA11 == "Yes"):
            entry = Scab(timestamp=dt.now(timezone.utc).date(), N=ScLWN, M=ScLWM, E=ScLWE, X=ScLWX, S=ScLWS, G=ScLWG, A16=ScLWA16, Y=ScLWY, A11=ScLWA11)
            db.session.add(entry)
            db.session.commit() # add to list of warnings
            print(Scab.query.order_by(Scab.timestamp.desc()).first().timestamp) 

        return{'ScLWN': ScLWN, 'ScLWM': ScLWM, 'ScLWE': ScLWE, 'ScLWX': ScLWX, 'ScLWG': ScLWG, 'ScLWA16': ScLWA16, 'ScLWY': ScLWY, 'ScLWA11': ScLWA11, 'ScLWS': ScLWS}

    except Exception as e:
        pprint(e)
    
    return{'ScLWN': "NA", 'ScLWM': "NA", 'ScLWE': "NA", 'ScLWX': "NA", 'ScLWG': "NA", 'ScLWA16': "NA", 'ScLWY': "NA", 'ScLWA11': "NA", 'ScLWS': "NA"}
    

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/temp')
def get_current_time():

    print("Starting temp")
    t = time.time()
    global abstime
    abstime = time.time()
    #Get most recent timestamp for Hobolink
    curTime = (dt.now(timezone.utc) - timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S')
    prevTime = (dt.now(timezone.utc) - timedelta(minutes=35)).strftime('%Y-%m-%d %H:%M:%S')
    utc_now = pytz.utc.localize(dt.utcnow())
    timestamp = utc_now.astimezone(pytz.timezone("US/Eastern")).strftime('%Y-%m-%d %H:%M:%S')


    #Initialize parameters for API
    url = "https://webservice.hobolink.com/restv2/data/json"

    values = {
        "action": "",
        "authentication": {
            "password": app.config['PASSWORD'],
            "token": app.config['TOKEN'],
            "user": app.config['USERNAME']
            # "password": config.password,
            # "token": config.token,
            # "user": config.username
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
            print("Got temp data at %d seconds"%(time.time()-t))

            #Convert response to a pandas dataframe
            data = json.loads(res.decode())
            df = pd.json_normalize(data['observationList'])

            #North air temperature
            if "20777735-1" in df.values:
                rowNA = df.loc[df['sensor_sn'] == "20777735-1"]
                valueNA = rowNA.iloc[-1]['us_value']
            else:
                valueNA = 0

            if "20683649-1" in df.values:
                ATM = df.loc[df['sensor_sn'] == "20683649-1"]
                valueATM = ATM.iloc[-1]['us_value']
            else:
                valueATM = 0
            
            if "20677838-1" in df.values:
                ATE = df.loc[df['sensor_sn'] == "20677838-1"]
                valueATE = ATE.iloc[-1]['us_value']
            else:
                valueATE = 0
                
            if "20683651-1" in df.values:
                ATX = df.loc[df['sensor_sn'] == "20683651-1"]
                valueATX = ATX.iloc[-1]['us_value']
            else:
                valueATX = 0

            #South air temperature
            if "20692768-1" in df.values:
                rowSA = df.loc[df['sensor_sn'] == "20692768-1"]
                valueSA = rowSA.iloc[-1]['us_value']
            else:
                valueSA = 0

            if "20677839-1" in df.values:
                ATG = df.loc[df['sensor_sn'] == "20677839-1"]
                valueATG = ATG.iloc[-1]['us_value']
            else:
                valueATG = 0    

            if "20677837-1" in df.values:
                ATA16 = df.loc[df['sensor_sn'] == "20677837-1"]
                valueATA16 = ATA16.iloc[-1]['us_value']
            else:
                valueATA16 = 0 

            if "20683650-1" in df.values:
                ATY = df.loc[df['sensor_sn'] == "20683650-1"]
                valueATY = ATY.iloc[-1]['us_value']
            else:
                valueATY = 0 

            if "20677836-1" in df.values:
                ATA11 = df.loc[df['sensor_sn'] == "20677836-1"]
                valueATA11 = ATA11.iloc[-1]['us_value']
            else:
                valueATA11 = 0 

            #RH North
            if "20777735-2" in df.values:
                RHN12 = df.loc[df['sensor_sn'] == "20777735-2"]
                valueRHN = RHN12.iloc[-1]['us_value']
            else:
                valueRHN = 0 

            if "20683649-2" in df.values:
                RHM = df.loc[df['sensor_sn'] == "20683649-2"]
                valueRHM = RHM.iloc[-1]['us_value']
            else:
                valueRHM = 0     

            if "20677838-2" in df.values:
                RHE = df.loc[df['sensor_sn'] == "20677838-2"]
                valueRHE = RHE.iloc[-1]['us_value']
            else:
                valueRHE = 0     

            if "20683651-2" in df.values:
                RHX = df.loc[df['sensor_sn'] == "20683651-2"]
                valueRHX = RHX.iloc[-1]['us_value']
            else:
                valueRHX = 0      
                
            #RH South
            if "20692768-2" in df.values:
                RHS12 = df.loc[df['sensor_sn'] == "20692768-2"]
                valueRHS = RHS12.iloc[-1]['us_value']
            else:
                valueRHS = 0 

            if "20677839-2" in df.values:
                RHG = df.loc[df['sensor_sn'] == "20677839-2"]
                valueRHG = RHG.iloc[-1]['us_value']
            else:
                valueRHG = 0     

            if "20677837-2" in df.values:
                RHA16 = df.loc[df['sensor_sn'] == "20677837-2"]
                valueRHA16 = RHA16.iloc[-1]['us_value']
            else:
                valueRHA16 = 0      

            if "20683650-2" in df.values:
                RHY = df.loc[df['sensor_sn'] == "20683650-2"]
                valueRHY = RHY.iloc[-1]['us_value']
            else:
                valueRHY = 0     

            if "20677836-2" in df.values:
                RHA11 = df.loc[df['sensor_sn'] == "20677836-2"]
                valueRHA11 = RHA11.iloc[-1]['us_value']
            else:
                valueRHA11 = 0     
                

            #Dew Point North
            if "20777735-3" in df.values:
                DPN = df.loc[df['sensor_sn'] == "20777735-3"]
                valueDPN = DPN.iloc[-1]['us_value']
            else:
                valueDPN = 0 

            if "20683649-3" in df.values:
                DPM = df.loc[df['sensor_sn'] == "20683649-3"]
                valueDPM = DPM.iloc[-1]['us_value']
            else:
                valueDPM = 0     

            if "20677838-3" in df.values:
                DPE = df.loc[df['sensor_sn'] == "20677838-3"]
                valueDPE = DPE.iloc[-1]['us_value']
            else:
                valueDPE = 0     

            if "20683651-3" in df.values:
                DPX = df.loc[df['sensor_sn'] == "20683651-3"]
                valueDPX = DPX.iloc[-1]['us_value']
            else:
                valueDPX = 0        

            #Dew Point South
            if "20692768-3" in df.values:
                DPS = df.loc[df['sensor_sn'] == "20692768-3"]
                valueDPS = DPS.iloc[-1]['us_value']
            else:
                valueDPS = 0 

            if "20677839-3" in df.values:
                DPG = df.loc[df['sensor_sn'] == "20677839-3"]
                valueDPG = DPG.iloc[-1]['us_value']
            else:
                valueDPG = 0     

            if "20677837-3" in df.values:
                DPA16 = df.loc[df['sensor_sn'] == "20677837-3"]
                valueDPA16 = DPA16.iloc[-1]['us_value']
            else:
                valueDPA16 = 0      

            if "20683650-3" in df.values:
                DPY = df.loc[df['sensor_sn'] == "20683650-3"]
                valueDPY = DPY.iloc[-1]['us_value']
            else:
                valueDPY = 0     

            if "20677836-3" in df.values:
                DPA11 = df.loc[df['sensor_sn'] == "20677836-3"]
                valueDPA11 = DPA11.iloc[-1]['us_value']
            else:
                valueDPA11 = 0    
        
            #Temperature soil North
            if "20770089-1" in df.values:
                TSN = df.loc[df['sensor_sn'] == "20770089-1"]
                valueTSN = TSN.iloc[-1]['us_value']
            else:
                valueTSN = 0 

            if "20683693-1" in df.values:
                TSM = df.loc[df['sensor_sn'] == "20683693-1"]
                valueTSM = TSM.iloc[-1]['us_value']
            else:
                valueTSM = 0     

            if "20683722-1" in df.values:
                TSE = df.loc[df['sensor_sn'] == "20683722-1"]
                valueTSE = TSE.iloc[-1]['us_value']
            else:
                valueTSE = 0     

            if "20683695-1" in df.values:
                TSX = df.loc[df['sensor_sn'] == "20683695-1"]
                valueTSX = TSX.iloc[-1]['us_value']
            else:
                valueTSX = 0  

            #Temperature soil South
            if "20684342-1" in df.values:
                TSS = df.loc[df['sensor_sn'] == "20684342-1"]
                valueTSS = TSS.iloc[-1]['us_value']
            else:
                valueTSS = 0 

            if "20683697-1" in df.values:
                TSG = df.loc[df['sensor_sn'] == "20683697-1"]
                valueTSG = TSG.iloc[-1]['us_value']
            else:
                valueTSG = 0     

            if "20683696-1" in df.values:
                TSA16 = df.loc[df['sensor_sn'] == "20683696-1"]
                valueTSA16 = TSA16.iloc[-1]['us_value']
            else:
                valueTSA16 = 0      

            if "20683694-1" in df.values:
                TSY = df.loc[df['sensor_sn'] == "20683694-1"]
                valueTSY = TSY.iloc[-1]['us_value']
            else:
                valueTSY = 0     

            if "20683723-1" in df.values:
                TSA11 = df.loc[df['sensor_sn'] == "20683723-1"]
                valueTSA11 = TSA11.iloc[-1]['us_value']
            else:
                valueTSA11 = 0 
        
            #Leaf Wetness North
            if "20774075-1" in df.values:
                LWN = df.loc[df['sensor_sn'] == "20774075-1"]
                valueLWN = LWN.iloc[-1]['us_value']
            else:
                valueLWN = 0 

            if "20776878-1" in df.values:
                LWM = df.loc[df['sensor_sn'] == "20776878-1"]
                valueLWM = LWM.iloc[-1]['us_value']
            else:
                valueLWM = 0     

            if "20778340-1" in df.values:
                LWE = df.loc[df['sensor_sn'] == "20778340-1"]
                valueLWE = LWE.iloc[-1]['us_value']
            else:
                valueLWE = 0     

            if "20780842-1" in df.values:
                LWX = df.loc[df['sensor_sn'] == "20780842-1"]
                valueLWX = LWX.iloc[-1]['us_value']
            else:
                valueLWX = 0 

            #Leaf Wetness South
            if "20650716-1" in df.values:
                LWS = df.loc[df['sensor_sn'] == "20650716-1"]
                valueLWS = LWS.iloc[-1]['us_value']
            else:
                valueLWS = 0 

            if "20778341-1" in df.values:
                LWG = df.loc[df['sensor_sn'] == "20778341-1"]
                valueLWG = LWG.iloc[-1]['us_value']
            else:
                valueLWG = 0     

            if "20776877-1" in df.values:
                LWA16 = df.loc[df['sensor_sn'] == "20776877-1"]
                valueLWA16 = LWA16.iloc[-1]['us_value']
            else:
                valueLWA16 = 0      

            if "20778339-1" in df.values:
                LWY = df.loc[df['sensor_sn'] == "20778339-1"]
                valueLWY = LWY.iloc[-1]['us_value']
            else:
                valueLWY = 0     

            if "20778342-1" in df.values:
                LWA11 = df.loc[df['sensor_sn'] == "20778342-1"]
                valueLWA11 = LWA11.iloc[-1]['us_value']
            else:
                valueLWA11 = 0 
                
            #Rain North
            if "20775973-1" in df.values:
                RN = df.loc[df['sensor_sn'] == "20775973-1"]
                valueRN = RN.iloc[-1]['us_value']
            else:
                valueRN = 0 

            if "20683599-1" in df.values:
                RM = df.loc[df['sensor_sn'] == "20683599-1"]
                valueRM = RM.iloc[-1]['us_value']
            else:
                valueRM = 0     

            if "20683600-1" in df.values:
                RE = df.loc[df['sensor_sn'] == "20683600-1"]
                valueRE = RE.iloc[-1]['us_value']
            else:
                valueRE = 0     

            if "20629502-1" in df.values:
                RX = df.loc[df['sensor_sn'] == "20629502-1"]
                valueRX = RX.iloc[-1]['us_value']
            else:
                valueRX = 0 

            #Rain South
            if "20696900-1" in df.values:
                RS = df.loc[df['sensor_sn'] == "20696900-1"]
                valueRS = RS.iloc[-1]['us_value']
            else:
                valueRS = 0 

            if "20810982-1" in df.values:
                RG = df.loc[df['sensor_sn'] == "20810982-1"]
                valueRG = RG.iloc[-1]['us_value']
            else:
                valueRG = 0     

            if "20683603-1" in df.values:
                RA16 = df.loc[df['sensor_sn'] == "20683603-1"]
                valueRA16 = RA16.iloc[-1]['us_value']
            else:
                valueRA16 = 0      

            if "20683602-1" in df.values:
                RY = df.loc[df['sensor_sn'] == "20683602-1"]
                valueRY = RY.iloc[-1]['us_value']
            else:
                valueRY = 0     

            if "20683601-1" in df.values:
                RA11 = df.loc[df['sensor_sn'] == "20683601-1"]
                valueRA11 = RA11.iloc[-1]['us_value']
            else:
                valueRA11 = 0 
        
            #Solar Radiation North
            if "20779661-1" in df.values:
                SRN = df.loc[df['sensor_sn'] == "20779661-1"]
                valueSRN = SRN.iloc[-1]['us_value']
            else:
                valueSRN = 0 

            if "20864948-1" in df.values:
                SRM = df.loc[df['sensor_sn'] == "20864948-1"]
                valueSRM = SRM.iloc[-1]['us_value']
            else:
                valueSRM = 0     

            if "20413294-1" in df.values:
                SRE = df.loc[df['sensor_sn'] == "20413294-1"]
                valueSRE = SRE.iloc[-1]['us_value']
            else:
                valueSRE = 0     

            if "20735859-1" in df.values:
                SRX = df.loc[df['sensor_sn'] == "20735859-1"]
                valueSRX = SRX.iloc[-1]['us_value']
            else:
                valueSRX = 0 

            #Solar Radiation South
            if "20683743-1" in df.values:
                SRS = df.loc[df['sensor_sn'] == "20683743-1"]
                valueSRS = SRS.iloc[-1]['us_value'] 
            else:
                valueSRS = 0 

            if "20413291-1" in df.values:
                SRG = df.loc[df['sensor_sn'] == "20413291-1"]
                valueSRG = SRG.iloc[-1]['us_value']
            else:
                valueSRG = 0     

            if "20413293-1" in df.values:
                SRA16 = df.loc[df['sensor_sn'] == "20413293-1"]
                valueSRA16 = SRA16.iloc[-1]['us_value']
            else:
                valueSRA16 = 0      

            if "20454637-1" in df.values:
                SRY = df.loc[df['sensor_sn'] == "20454637-1"]
                valueSRY = SRY.iloc[-1]['us_value']
            else:
                valueSRY = 0     

            if "20413295-1" in df.values:
                SRA11 = df.loc[df['sensor_sn'] == "20413295-1"]
                valueSRA11 = SRA11.iloc[-1]['us_value']
            else:
                valueSRA11 = 0 

            #Water Content Soil North
            if "20773509-1" in df.values:
                WCSN = df.loc[df['sensor_sn'] == "20773509-1"]
                valueWCSN = WCSN.iloc[-1]['us_value']
            else:
                valueWCSN = 0 

            if "20683612-1" in df.values:
                WCM = df.loc[df['sensor_sn'] == "20683612-1"]
                valueWCM = WCM.iloc[-1]['us_value']
            else:
                valueWCM = 0     

            if "20683614-1" in df.values:
                WCE = df.loc[df['sensor_sn'] == "20683614-1"]
                valueWCE = WCE.iloc[-1]['us_value']
            else:
                valueWCE = 0     

            if "20683610-1" in df.values:
                WCX = df.loc[df['sensor_sn'] == "20683610-1"]
                valueWCX = WCX.iloc[-1]['us_value']
            else:
                valueWCX = 0  

            #Water Content Soil South
            if "20696181-1" in df.values:
                WCSS = df.loc[df['sensor_sn'] == "20696181-1"]
                valueWCSS = WCSS.iloc[-1]['us_value']
            else:
                valueWCSS = 0 

            if "20683611-1" in df.values:
                WCG = df.loc[df['sensor_sn'] == "20683611-1"]
                valueWCG = WCG.iloc[-1]['us_value']
            else:
                valueWCG = 0     

            if "20543770-1" in df.values:
                WCA16 = df.loc[df['sensor_sn'] == "20543770-1"] #confirm wca values, switch a11 and a16?
                valueWCA16 = WCA16.iloc[-1]['us_value']
            else:
                valueWCA16 = 0      

            if "20683609-1" in df.values:
                WCY = df.loc[df['sensor_sn'] == "20683609-1"]
                valueWCY = WCY.iloc[-1]['us_value']
            else:
                valueWCY = 0     

            if "20683615-1" in df.values:
                WCA11 = df.loc[df['sensor_sn'] == "20683615-1"]
                valueWCA11 = WCA11.iloc[-1]['us_value'] 
            else:
                valueWCA11 = 0 

            #Wind Speeds North
            if "20772423-1" in df.values:
                WSN = df.loc[df['sensor_sn'] == "20772423-1"]
                valueWSN = WSN.iloc[-1]['us_value']
            else:
                valueWSN = 0 

            if "20696852-1" in df.values:
                WSM = df.loc[df['sensor_sn'] == "20696852-1"]
                valueWSM = WSM.iloc[-1]['us_value']
            else:
                valueWSM = 0     

            if "20657340-1" in df.values:
                WSE = df.loc[df['sensor_sn'] == "20657340-1"]
                valueWSE = WSE.iloc[-1]['us_value']
            else:
                valueWSE = 0     

            if "20696851-1" in df.values:
                WSX = df.loc[df['sensor_sn'] == "20696851-1"]
                valueWSX = WSX.iloc[-1]['us_value']
            else:
                valueWSX = 0 

            #Wind Speeds South
            if "20673566-1" in df.values:
                WSS = df.loc[df['sensor_sn'] == "20673566-1"]
                valueWSS = WSS.iloc[-1]['us_value']
            else:
                valueWSS = 0 

            if "20657341-1" in df.values:
                WSG = df.loc[df['sensor_sn'] == "20657341-1"]
                valueWSG = WSG.iloc[-1]['us_value']
            else:
                valueWSG = 0     

            if "20696853-1" in df.values:
                WSA16 = df.loc[df['sensor_sn'] == "20696853-1"]
                valueWSA16 = WSA16.iloc[-1]['us_value']
            else:
                valueWSA16 = 0      

            if "20851758-1" in df.values:
                WSY = df.loc[df['sensor_sn'] == "20851758-1"]
                valueWSY = WSY.iloc[-1]['us_value']
            else:
                valueWSY = 0     

            if "20696855-1" in df.values:
                WSA11 = df.loc[df['sensor_sn'] == "20696855-1"]
                valueWSA11 = WSA11.iloc[-1]['us_value']
            else:
                valueWSA11 = 0 

            #Gust Speeds North
            if "20772423-2" in df.values:
                GSN = df.loc[df['sensor_sn'] == "20772423-2"]
                valueGSN = GSN.iloc[-1]['us_value']
            else:
                valueGSN = 0 

            if "20696852-2" in df.values:
                GSM = df.loc[df['sensor_sn'] == "20696852-2"]
                valueGSM = GSM.iloc[-1]['us_value']
            else:
                valueGSM = 0     

            if "20657340-2" in df.values:
                GSE = df.loc[df['sensor_sn'] == "20657340-2"]
                valueGSE = GSE.iloc[-1]['us_value']
            else:
                valueGSE = 0     

            if "20696851-1" in df.values:
                GSX = df.loc[df['sensor_sn'] == "20696851-2"]
                valueGSX = GSX.iloc[-1]['us_value']
            else:
                valueGSX = 0 

            #Gust Speeds South
            if "20673566-2" in df.values:
                GSS = df.loc[df['sensor_sn'] == "20673566-2"]
                valueGSS = GSS.iloc[-1]['us_value']
            else:
                valueGSS = 0 

            if "20657341-2" in df.values:
                GSG = df.loc[df['sensor_sn'] == "20657341-2"]
                valueGSG = GSG.iloc[-1]['us_value']
            else:
                valueGSG = 0     

            if "20696853-2" in df.values:
                GSA16 = df.loc[df['sensor_sn'] == "20696853-2"]
                valueGSA16 = GSA16.iloc[-1]['us_value']
            else:
                valueGSA16 = 0      

            if "20851758-2" in df.values:
                GSY = df.loc[df['sensor_sn'] == "20851758-2"]
                valueGSY = GSY.iloc[-1]['us_value']
            else:
                valueGSY = 0     

            if "20696855-2" in df.values:
                GSA11 = df.loc[df['sensor_sn'] == "20696855-2"]
                valueGSA11 = GSA11.iloc[-1]['us_value']
            else:
                valueGSA11 = 0 

            #Wind Direction North (don't round)
            if "20774012-1" in df.values:
                WDN = df.loc[df['sensor_sn'] == "20774012-1"]
                valueWDN = WDN.iloc[-1]['us_value']
            else:
                valueWDN = 0 

            if "20696852-3" in df.values:
                WDM = df.loc[df['sensor_sn'] == "20696852-3"]
                valueWDM = WDM.iloc[-1]['us_value']
            else:
                valueWDM = 0     

            if "20657340-3" in df.values:
                WDE = df.loc[df['sensor_sn'] == "20657340-3"]
                valueWDE = WDE.iloc[-1]['us_value']
            else:
                valueWDE = 0     

            if "20696851-3" in df.values:
                WDX = df.loc[df['sensor_sn'] == "20696851-3"]
                valueWDX = WDX.iloc[-1]['us_value']
            else:
                valueWDX = 0      

            #Wind Direction South (don't round)
            if "20677657-1" in df.values:
                WDS = df.loc[df['sensor_sn'] == "20677657-1"]
                valueWDS = WDS.iloc[-1]['us_value']
            else:
                valueWDS = 0 

            if "20657341-3" in df.values:
                WDG = df.loc[df['sensor_sn'] == "20657341-3"]
                valueWDG = WDG.iloc[-1]['us_value']
            else:
                valueWDG = 0     

            if "20696853-3" in df.values:
                WDA16 = df.loc[df['sensor_sn'] == "20696853-3"]
                valueWDA16 = WDA16.iloc[-1]['us_value']
            else:
                valueWDA16 = 0      

            if "20851758-3" in df.values:
                WDY = df.loc[df['sensor_sn'] == "20851758-3"]
                valueWDY = WDY.iloc[-1]['us_value']
            else:
                valueWDY = 0     

            if "20696855-3" in df.values:
                WDA11 = df.loc[df['sensor_sn'] == "20696855-3"]
                valueWDA11 = WDA11.iloc[-1]['us_value']
            else:
                valueWDA11 = 0 
        
            print("Finishing temp api at %d seconds"%(time.time()-t))
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
            'time': timestamp
            }
    except Exception as e:
        print(e)
    
    print("Finishing temp api at %d seconds"%(time.time()-t))   
    return {
        'tempN': "%.2f" % 0, 'tempS': "%.2f" % 0,
            'RHN': "%.2f" % 0, 'RHS': "%.2f" % 0,
            'TSN': "%.2f" % 0, 'TSS': "%.2f" % 0,
            'LWN': "%.2f" % 0, 'LWS': "%.2f" % 0,
            'DPN': "%.2f" % 0, 'DPS': "%.2f" % 0,
            'RN': "%.2f" % 0, 'RS': "%.2f" % 0,
            'SRN': "%.2f" % 0, 'SRS': "%.2f" % 0,
            'WCSN': "%.2f" % 0, 'WCSS': "%.2f" % 0,
            'ATM': "%.2f" % 0, 'ATE': "%.2f" % 0, 'ATX': "%.2f" % 0,
            'ATG': "%.2f" % 0, 'ATA16': "%.2f" % 0, 'ATY': "%.2f" % 0, 'ATA11': "%.2f" % 0,
            'RHM': "%.2f" % 0, 'RHE': "%.2f" % 0, 'RHX': "%.2f" % 0,
            'RHG': "%.2f" % 0, 'RHA16': "%.2f" % 0, 'RHY': "%.2f" % 0, 'RHA11': "%.2f" % 0,
            'DPM': "%.2f" % 0, 'DPE': "%.2f" % 0, 'DPX': "%.2f" % 0,
            'DPG': "%.2f" % 0, 'DPA16': "%.2f" % 0, 'DPY': "%.2f" % 0, 'DPA11': "%.2f" % 0,
            'TSM': "%.2f" % 0, 'TSE': "%.2f" % 0, 'TSX': "%.2f" % 0,
            'TSG': "%.2f" % 0, 'TSA16': "%.2f" % 0, 'TSY': "%.2f" % 0, 'TSA11': "%.2f" % 0,
            'LWM': "%.2f" % 0, 'LWE': "%.2f" % 0, 'LWX': "%.2f" % 0,
            'LWG': "%.2f" % 0, 'LWA16': "%.2f" % 0, 'LWY': "%.2f" % 0, 'LWA11': "%.2f" % 0,
            'RM': "%.2f" % 0, 'RE': "%.2f" % 0, 'RX': "%.2f" % 0,
            'RG': "%.2f" % 0, 'RA16': "%.2f" % 0, 'RY': "%.2f" % 0, 'RA11': "%.2f" % 0,
            'SRM': "%.2f" % 0, 'SRE': "%.2f" % 0, 'SRX': "%.2f" % 0,
            'SRG': "%.2f" % 0, 'SRA16': "%.2f" % 0, 'SRY': "%.2f" % 0, 'SRA11': "%.2f" % 0,
            'WCM': "%.2f" % 0, 'WCE': "%.2f" % 0, 'WCX': "%.2f" % 0,
            'WCG': "%.2f" % 0, 'WCA16': "%.2f" % 0, 'WCY': "%.2f" % 0, 'WCA11': "%.2f" % 0,
            'WSN': "%.2f" % 0, 'WSM': "%.2f" % 0, 'WSE': "%.2f" % 0, 'WSX': "%.2f" % 0,
            'WSS': "%.2f" % 0,'WSG': "%.2f" % 0, 'WSA16': "%.2f" % 0, 'WSY': "%.2f" % 0, 'WSA11': "%.2f" % 0,
            'GSN': "%.2f" % 0, 'GSM': "%.2f" % 0, 'GSE': "%.2f" % 0, 'GSX': "%.2f" % 0,
            'GSS': "%.2f" % 0,'GSG': "%.2f" % 0, 'GSA16': "%.2f" % 0, 'GSY': "%.2f" % 0, 'GSA11': "%.2f" % 0,
            'WDN': "%.2f" % 0, 'WDM': "%.2f" % 0, 'WDE': "%.2f" % 0, 'WDX': "%.2f" % 0,
            'WDS': "%.2f" % 0, 'WDG':"%.2f" % 0, 'WDA16': "%.2f" % 0, 'WDY':"%.2f" % 0, 'WDA11': "%.2f" % 0,
            'time': "Could not connect to the weather station"
    }
 

@app.route('/api/scab')
def apple_scab():
    return getscab()

@app.route('/api/scabDB')
def apple_scab_warnings():
    warnings = str(Scab.query.order_by(Scab.timestamp.desc()).first().timestamp)
    if warnings is None:
        return ""
    return warnings

@app.route('/api/download', methods=['POST'])
def download():
    data = request.json
    options = data["values"]
    print(options)
    curTime = dt.strptime(data["endingDate"]+" "+data["endingTime"]+":00.0000", '%Y-%m-%d %H:%M:%S.%f').astimezone(pytz.utc).strftime("%Y-%m-%d %H:%M:%S")
    prevTime = dt.strptime(data["startingDate"]+" "+data["startingTime"]+":00.0000", '%Y-%m-%d %H:%M:%S.%f').astimezone(pytz.utc).strftime("%Y-%m-%d %H:%M:%S")
    
    #Specify values

    url = "https://webservice.hobolink.com/restv2/data/json"

    values = {
    "action": "",
    "authentication": {
        "password": app.config['PASSWORD'],
        "token": app.config['TOKEN'],
        "user": app.config['USERNAME']
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
        print("Success")

        data = json.loads(res.decode())
        # retData = json.dumps(data['observationList'])
        df = pd.json_normalize(data['observationList'])

        rows = []
        for i in options:
            if i['value'] in sensors:
                rows = rows + sensors[i['value']] # create a list of all sensor values
        x = df.loc[df['sensor_sn'].isin(rows)]

        retData = x.to_json(orient="records")
        print(type(retData))
        # print(df)
        return retData
    except Exception as e:
        pprint(e)
    
    return 500
