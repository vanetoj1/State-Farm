# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:24:16 2021

@author: User
"""


from __future__ import print_function

import requests

from requests.auth import HTTPBasicAuth
import datetime 
from datetime import datetime, timedelta



today = datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-7] 
headers = {"Content-Type": "image/png","MAC":"54:10:EC:B6:D8:98" }

response = requests.get('http://192.168.254.11/api/maps/startstop/export?&from=2020-05-15T09:00:00&to={}'.format(today), headers=headers,auth=HTTPBasicAuth('Admin', 'dimin3421'))
                        
image = response.content
import io
from PIL import Image

image3 = Image.open(io.BytesIO(image))
image3.show()