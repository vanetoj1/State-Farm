# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:29:21 2021

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

headers_op = { 'Content-Type': 'application/json','MAC':'80:1F:12:76:4B:DC'}



response_op = requests.get('http://192.168.254.19/api/data/historical/zone/dwell/summary?element=Zone 0&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers_op,auth=HTTPBasicAuth('Admin', 'dimin3421'))
response2_op = requests.get('http://192.168.254.19/api/data/historical/line/count?element=Line 0&format=json&from=2020-05-15T09:00:00&to={}&granularity=ONE_HOUR'.format(today), headers=headers_op,auth=HTTPBasicAuth('Admin', 'dimin3421'))
#api/data/historical/line/count?element=Line 0
#api/data/historical/line/count?element=Line 0

j_data_op = response_op.json()
print(response_op.content)
j_data2_op=response2_op.json()