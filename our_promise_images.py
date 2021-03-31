# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:20:48 2021

@author: User
"""


from __future__ import print_function

import requests

from requests.auth import HTTPBasicAuth
import datetime 
from datetime import datetime, timedelta



today = datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-7] 
headers = {"Content-Type": "image/png","MAC":"54:10:EC:B6:D1:38" }

response = requests.get('http://192.168.254.15/api/maps/startstop/export?&from=2020-05-15T09:00:00&to={}'.format(today), headers=headers,auth=HTTPBasicAuth('Admin', 'dimin3421'))
                        
image = response.content
import io
from PIL import Image

image4 = Image.open(io.BytesIO(image))
image4.show()
image4.save('C:/Users/User/Documents/My Tableau Repository/Shapes/MyImages/our_promise.png')

import boto3
s3 = boto3.resource('s3')

# Upload the file
# change `image.png` to whatever you want the file to be called

s3.Object('di-statefarm', 'analytics/our_promise.png').put(ACL="public-read", ContentDisposition="inline", ContentType="image/png", Body=open('C:/Users/User/Documents/My Tableau Repository/Shapes/MyImages/our_promise.png', 'rb'))