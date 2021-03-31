# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:36:56 2021

@author: User
"""


from __future__ import print_function

import requests

from requests.auth import HTTPBasicAuth
import datetime 
from datetime import datetime, timedelta



today = datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-7] 


headers = {"Content-Type": "image/png","MAC":"80:1F:12:76:4B:E2" }

response = requests.get('http://192.168.254.20/api/maps/startstop/export?&from=2020-05-28T10:00:00&to={}'.format(today), headers=headers,auth=HTTPBasicAuth('Admin', 'dimin3421'))
                        
image = response.content
import io
from PIL import Image

image31 = Image.open(io.BytesIO(image))
image31.show()