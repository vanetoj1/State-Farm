# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 12:27:28 2021

@author: User
"""


from __future__ import print_function

import requests

from requests.auth import HTTPBasicAuth

import datetime 
from datetime import datetime, timedelta



today = datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-7] 

#N = 7

#date_N_days_ago = datetime.today() - timedelta(days=N) 
#week_ago=date_N_days_ago.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-7]

headers_oi = { 'Content-Type': 'application/json','MAC':'54:10:EC:B6:FD:60'}



response_oi = requests.get('http://192.168.254.11/api/data/historical/zone/dwell/summary?element=Zone 0&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers_oi,auth=HTTPBasicAuth('Admin', 'dimin3421'))
#try:
  #  json_data = response.json()
 #   print(json_data.content)

#except ValueError:
    #print("Response content is not valid

j_data_oi = response_oi.json()
#print(response.content)

response_oi2 = requests.get('http://192.168.254.11/api/data/historical/zone/inoutcount?element=Zone 0&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers_oi,auth=HTTPBasicAuth('Admin', 'dimin3421'))

j_data_oi2 = response_oi2.json()

in_number_oi=[]
out_number_oi=[]

for results2 in j_data_oi2['content']['element'][0]['measurement']:
    in_number_oi.append(results2['value'][0]['value'])
for results3 in j_data_oi2['content']['element'][0]['measurement']:
    out_number_oi.append(results3['value'][1]['value'])
    
    
time_oi=[]
counts_oi=[]

stat_oi=[]
for result in j_data_oi['content']['element'][0]['measurement']:
    time_oi.append(result['from'])
for results2 in j_data_oi['content']['element'][0]['measurement']:
    stat_oi.append(results2['value'][0]['value'])
for results in j_data_oi['content']['element'][0]['measurement']:
    counts_oi.append(results2['value'][1]['value'])
    import pandas as pd
data_oi = pd.DataFrame(time_oi, columns=['Time'])
data_oi['Counts All']= pd.DataFrame(in_number_oi)

data_oi['Counts']= pd.DataFrame(counts_oi)
data_oi['Stat']=pd.DataFrame(stat_oi)
data_oi=data_oi.fillna(0)

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests

#change this by your sheet ID
SAMPLE_SPREADSHEET_ID_input = '1kUahG86CFtDXU8KH_-j6yoNlfQn9M2JKt-I4rnqGMtI'

#change the range if needed
SAMPLE_RANGE_NAME = 'A:D'

def Create_Service(client_secret_file, api_service_name, api_version, *scopes):
    global service
    SCOPES = [scope for scope in scopes[0]]
    #print(SCOPES)
    
    cred = None

    if os.path.exists('token_write.pickle'):
        with open('token_write.pickle', 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, SCOPES)
            cred = flow.run_local_server()

        with open('token_write.pickle', 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(api_service_name, api_version, credentials=cred)
        print(api_service_name, 'service created successfully')
        #return service
    except Exception as e:
        print(e)
        #return None
        
# change 'my_json_file.json' by your downloaded JSON file.
Create_Service('credentials.json', 'sheets', 'v4',['https://www.googleapis.com/auth/spreadsheets'])
    
def Export_Data_To_Sheets():
    
    response_date = service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
        valueInputOption='RAW',
        range=SAMPLE_RANGE_NAME,
        body=dict(
            majorDimension='ROWS',
            values=data_oi.values.tolist())
    ).execute()
    print('Sheet successfully Updated')

Export_Data_To_Sheets()