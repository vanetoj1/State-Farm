# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 11:58:57 2021

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




headers_ocp = { 'Content-Type': 'application/json','MAC':'54:10:EC:B6:E7:47'}



response_ocp = requests.get('http://192.168.254.12/api/data/historical/line/count?element=Line 0&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers_ocp,auth=HTTPBasicAuth('Admin', 'dimin3421'))
#try:
  #  json_data = response.json()
 #   print(json_data.content)

#except ValueError:
    #print("Response content is not valid

json_data_ocp = response_ocp.json()
print(response_ocp.content)

response2_ocp = requests.get('http://192.168.254.12/api/data/historical/zone/dwell/summary?element=Zone 0&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR&format=json'.format(today), headers=headers_ocp,auth=HTTPBasicAuth('Admin', 'dimin3421'))
ja_data_ocp=response2_ocp.json()


stat_all_ocp=[]
counts_all_ocp=[]

for results2 in ja_data_ocp['content']['element'][0]['measurement']:
    stat_all_ocp.append(results2['value'][0]['value'])
for results in ja_data_ocp['content']['element'][0]['measurement']:
    counts_all_ocp.append(results2['value'][1]['value'])
    
time_ocp=[]
counts_ocp=[]
for result in json_data_ocp['content']['element'][0]['measurement']:
    time_ocp.append(result['from'])
for results in json_data_ocp['content']['element'][0]['measurement']:
    counts_ocp.append(results['value'][0]['value'])
import pandas as pd
data_ocp = pd.DataFrame(time_ocp, columns=['Time'])
data_ocp['Counts all']= pd.DataFrame(counts_ocp)
data_ocp['Counts zone']= pd.DataFrame(counts_all_ocp)
data_ocp['Stats']= pd.DataFrame(stat_all_ocp)
data_ocp=data_ocp.fillna(0)



from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests

#change this by your sheet ID
SAMPLE_SPREADSHEET_ID_input = '1R2Jwx1eD5Fc-whplRiUCMx0SL-vUOSsrcDTHgW1h42A'

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
            values=data_ocp.values.tolist())
    ).execute()
    print('Sheet successfully Updated')

Export_Data_To_Sheets()