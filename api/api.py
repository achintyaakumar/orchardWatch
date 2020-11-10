import time
from flask import Flask
import urllib.request
import json
import pandas as pd
from pprint import pprint
import config

url = "https://webservice.hobolink.com/restv2/data/json"

values = {
  "action": "",
  "authentication": {
    "password": config.password,
    "token": config.token,
    "user": config.username
  },
  "query": {
    "end_date_time": "2020-10-10 12:05:00",
    "loggers": [20777720,20699245,1],
    "start_date_time": "2020-10-10 12:00:00"
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
row = df.loc[df['sensor_sn'] == "20777735-1"]
value = row.iloc[0]['si_value']

app = Flask(__name__)

@app.route('/temp')
def get_current_time():
    return {'temp': float(value)}