# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 09:53:35 2021

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

headers_com = { 'Content-Type': 'application/json','MAC':'54:10:EC:B6:D1:38'}



response_com= requests.get('http://192.168.254.15/api/data/historical/zone/inoutcount?element=our_community_all&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers_com,auth=HTTPBasicAuth('Admin', 'dimin3421'))
#try:
  #  json_data = response.json()
 #   print(json_data.content)

#except ValueError:
    #print("Response content is not valid

json_data_com = response_com.json()
print(response_com.content)

times_com=[]

in_number_com=[]
out_number_com=[]

for result1 in json_data_com['content']['element'][0]['measurement']:
    times_com.append(result1['from'])
for results2 in json_data_com['content']['element'][0]['measurement']:
    in_number_com.append(results2['value'][0]['value'])
for results3 in json_data_com['content']['element'][0]['measurement']:
    out_number_com.append(results3['value'][1]['value'])

response_all_com = requests.get('http://192.168.254.15/api/data/historical/zone/dwell/summary?element=our_community_all&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers_com,auth=HTTPBasicAuth('Admin', 'dimin3421'))
ja_data_com=response_all_com.json()
print(response_all_com.content)

stat_all_com=[]
counts_all_com=[]

for results2 in ja_data_com['content']['element'][0]['measurement']:
    stat_all_com.append(results2['value'][0]['value'])
for results in ja_data_com['content']['element'][0]['measurement']:
    counts_all_com.append(results2['value'][1]['value'])
    
import pandas as pd
data_com = pd.DataFrame(times_com, columns=['Time_com'])
data_com['Counts_line_com']= pd.DataFrame(in_number_com)
data_com['Counts_dwell_com']= pd.DataFrame(counts_all_com)
data_com['Stat_com']= pd.DataFrame(stat_all_com)
data_com=data_com.fillna(0)

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests

#change this by your sheet ID
SAMPLE_SPREADSHEET_ID_input = '1CBrA9LFEy4Am6HUappLKJD07S88KUgzPwxOHL7ybw04'

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
            values=data_com.values.tolist())
    ).execute()
    print('Sheet successfully Updated')

Export_Data_To_Sheets()