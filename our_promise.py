# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:09:28 2021

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




headers_opr = { 'Content-Type': 'application/json','MAC':'54:10:EC:B6:D1:38'}



response_opr = requests.get('http://192.168.254.15/api/data/historical/line/count?element=our_promise&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers_opr,auth=HTTPBasicAuth('Admin', 'dimin3421'))


j_data_opr = response_opr.json()
print(response_opr.content)

time_opr=[]
counts_line_opr=[]
for result in j_data_opr['content']['element'][0]['measurement']:
    time_opr.append(result['from'])
for results in j_data_opr['content']['element'][0]['measurement']:
    counts_line_opr.append(results['value'][0]['value'])
time_opr=[]
counts_line_opr=[]
for result in j_data_opr['content']['element'][0]['measurement']:
    time_opr.append(result['from'])
for results in j_data_opr['content']['element'][0]['measurement']:
    counts_line_opr.append(results['value'][0]['value'])

response2_opr = requests.get('http://192.168.254.15/api/data/historical/zone/dwell/summary?element=our_promise2&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers_opr,auth=HTTPBasicAuth('Admin', 'dimin3421'))
j_data2_opr=response2_opr.json()
print(response2_opr.content)

response3 = requests.get('http://192.168.254.15/api/data/historical/zone/inoutcount?element=promise_all&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers_opr,auth=HTTPBasicAuth('Admin', 'dimin3421'))
j_data_opr3=response3.json()
print(response3.content)

response_all_opr = requests.get('http://192.168.254.15/api/data/historical/zone/dwell/summary?element=promise_all&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers_opr,auth=HTTPBasicAuth('Admin', 'dimin3421'))
j_data_opr4=response_all_opr.json()
print(response_all_opr.content)

stat_all_opr=[]
counts_all_opr=[]

for results2 in j_data_opr4['content']['element'][0]['measurement']:
    stat_all_opr.append(results2['value'][0]['value'])
for results in j_data_opr4['content']['element'][0]['measurement']:
    counts_all_opr.append(results2['value'][1]['value'])
    
in_number_opr=[]
out_number_opr=[]
times_opr=[]
for result1 in j_data_opr3['content']['element'][0]['measurement']:
    times_opr.append(result1['from'])
for results2 in j_data_opr3['content']['element'][0]['measurement']:
    in_number_opr.append(results2['value'][0]['value'])
for results3 in j_data_opr3['content']['element'][0]['measurement']:
    out_number_opr.append(results3['value'][1]['value'])
    
response3_opr = requests.get('http://192.168.254.15/api/data/historical/zone/dwell/summary?element=our_promise3&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers_opr,auth=HTTPBasicAuth('Admin', 'dimin3421'))
j_data3_opr=response3_opr.json()
print(response3_opr.content)

response1_opr = requests.get('http://192.168.254.15/api/data/historical/zone/dwell/summary?element=our_promise1&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers_opr,auth=HTTPBasicAuth('Admin', 'dimin3421'))
j_data1_opr=response1_opr.json()
print(response1_opr.content)

stat1_opr=[]
counts1_zone_opr=[]

for results2 in j_data1_opr['content']['element'][0]['measurement']:
    stat1_opr.append(results2['value'][0]['value'])
for results in j_data1_opr['content']['element'][0]['measurement']:
    counts1_zone_opr.append(results2['value'][1]['value'])
    
stat2_opr=[]
counts2_zone_opr=[]

for results2 in j_data2_opr['content']['element'][0]['measurement']:
    stat2_opr.append(results2['value'][0]['value'])
for results in j_data2_opr['content']['element'][0]['measurement']:
    counts2_zone_opr.append(results2['value'][1]['value'])
    
stat3_opr=[]
counts3_zone_opr=[]

for results2 in j_data3_opr['content']['element'][0]['measurement']:
    stat3_opr.append(results2['value'][0]['value'])
for results in j_data3_opr['content']['element'][0]['measurement']:
    counts3_zone_opr.append(results2['value'][1]['value'])
    
import pandas as pd
data_opr = pd.DataFrame(times_opr, columns=['Time'])
data_opr['Counts_line']= pd.DataFrame(in_number_opr)
data_opr['Counts_all_zone']= pd.DataFrame(counts_all_opr)

data_opr['Stat_all']= pd.DataFrame(stat_all_opr)

data_opr['Counts1_zone']= pd.DataFrame(counts1_zone_opr)
data_opr['Counts2_zone']= pd.DataFrame(counts2_zone_opr)
data_opr['Counts3_zone']= pd.DataFrame(counts3_zone_opr)

data_opr['Stat1']= pd.DataFrame(stat1_opr)
data_opr['Stat2']= pd.DataFrame(stat2_opr)
data_opr['Stat3']= pd.DataFrame(stat3_opr)
data_opr=data_opr.fillna(0)

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests

#change this by your sheet ID
SAMPLE_SPREADSHEET_ID_input = '17rb-vbj9EfMGf0eG50z3OWDuMWjUhHCp0LxavfsSjoQ'
                                
#change the range if needed
SAMPLE_RANGE_NAME = 'A:J'

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
            values=data_opr.values.tolist())
    ).execute()
    print('Sheet successfully Updated')

Export_Data_To_Sheets()