# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 08:57:48 2021

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

headers_os = { 'Content-Type': 'application/json','MAC':'54:10:EC:B6:E6:E8'}

r_dw=requests.get('http://192.168.254.14/api/data/historical/zone/dwell/summary?element=Zone 0&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today),auth=HTTPBasicAuth('Admin', 'dimin3421'))



#response = requests.get('http://192.168.254.14/api/data/historical/zone/count?element=Zone 0&format=json&from=2020-05-15T09:00:00&to=2020-07-31T17:00:00&granularity=ONE_MINUTE', headers=headers,auth=HTTPBasicAuth('Admin', 'dimin3421'))
#try
  #  json_data = response.json()
 #   print(json_data.content)

#except ValueError:
    #print("Response content is not valid

j_data_os = r_dw.json()
print(r_dw.content)


r_dw2=requests.get('http://192.168.254.14/api/data/historical/zone/inoutcount?element=Zone 0&format=json&from=2020-05-15T10:00:00&to=2020-09-29T17:00:00&granularity=ONE_HOUR',auth=HTTPBasicAuth('Admin', 'dimin3421'))

in_number_os=[]
out_number_os=[]


for results2 in j_data_os['content']['element'][0]['measurement']:
    in_number_os.append(results2['value'][0]['value'])
for results3 in j_data_os['content']['element'][0]['measurement']:
    out_number_os.append(results3['value'][1]['value'])
    
import pandas as pd
data_os = pd.DataFrame(time_os, columns=['Time'])
data_os['Counts All']= pd.DataFrame(in_number_os)

data_os['Counts']= pd.DataFrame(counts_os)
data_os['Stat']= pd.DataFrame(stat_os)

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests

#change this by your sheet ID
SAMPLE_SPREADSHEET_ID_input = '1Z-mtvOCwUYS4qIH3WwjsdPZcV0HMU-oWHESF387_1fI'

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
            values=data_os.values.tolist())
    ).execute()
    print('Sheet successfully Updated')

Export_Data_To_Sheets()