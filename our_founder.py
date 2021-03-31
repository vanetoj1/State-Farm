# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 12:12:52 2021

@author: User
"""



from __future__ import print_function

import requests

from requests.auth import HTTPBasicAuth

import datetime 
from datetime import datetime, timedelta
import datetime 
from datetime import datetime, timedelta



today = datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-7] 





headers = { 'Content-Type': 'application/json','MAC':'54:10:EC:B6:E4:58'}


response_of1= requests.get('http://192.168.254.17/api/data/historical/zone/inoutcount?element=Zone all&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers,auth=HTTPBasicAuth('Admin', 'dimin3421'))
response_of = requests.get('http://192.168.254.17/api/data/historical/zone/dwell/summary?element=Zone 0&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers,auth=HTTPBasicAuth('Admin', 'dimin3421'))
response2_of= requests.get('http://192.168.254.17/api/data/historical/zone/dwell/summary?element=Zone 1&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers,auth=HTTPBasicAuth('Admin', 'dimin3421'))



j_data_of1 = response_of1.json()

response_of1.content
j_data_of = response_of.json()
print(response_of.content)
j_data_of2=response2_of.json()

in_number_of=[]
out_number_of=[]

for results2 in j_data_of1['content']['element'][0]['measurement']:
    in_number_of.append(results2['value'][0]['value'])
for results3 in j_data_of1['content']['element'][0]['measurement']:
    out_number_of.append(results3['value'][1]['value'])
    
time_of=[]
stat_of=[]
counts_of=[]
for result in j_data_of['content']['element'][0]['measurement']:
    time_of.append(result['from'])
for results2 in j_data_of['content']['element'][0]['measurement']:
    stat_of.append(results2['value'][0]['value'])
for results in j_data_of['content']['element'][0]['measurement']:
    counts_of.append(results2['value'][1]['value'])
    import pandas as pd
data_of = pd.DataFrame(time_of, columns=['Time'])
data_of['Counts in']= pd.DataFrame(in_number_of)

data_of['Counts']= pd.DataFrame(counts_of)
data_of['Stat']=pd.DataFrame(stat_of)

time_of2=[]
stat_of2=[]
counts_of2=[]
for result in j_data_of2['content']['element'][0]['measurement']:
    time_of2.append(result['from'])
for results2 in j_data_of2['content']['element'][0]['measurement']:
    stat_of2.append(results2['value'][0]['value'])
for results in j_data_of2['content']['element'][0]['measurement']:
    counts_of2.append(results2['value'][1]['value'])
    import pandas as pd
data_of['Counts2']= pd.DataFrame(counts_of2)
data_of['Stat2']=pd.DataFrame(stat_of2)

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests

#change this by your sheet ID
SAMPLE_SPREADSHEET_ID_input = '1pNCGXjocV22GYinuI6m-UyP9ubSgJB53rU0yY7ctcz4'

#change the range if needed
SAMPLE_RANGE_NAME = 'A:F'

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
            values=data_of.values.tolist())
    ).execute()
    print('Sheet successfully Updated')

Export_Data_To_Sheets()
