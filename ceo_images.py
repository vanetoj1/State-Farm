# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:53:13 2021

@author: User
"""


from __future__ import print_function

import requests

from requests.auth import HTTPBasicAuth
import datetime 
from datetime import datetime, timedelta



today = datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-7] 

headers = {"Content-Type": "image/png","MAC":"54:10:EC:B6:E7:56" }

response = requests.get('http://192.168.254.16/api/maps/startstop/export?&from=2020-05-15T09:00:00&to={}'.format(today), headers=headers,auth=HTTPBasicAuth('Admin', 'dimin3421'))
                        
image = response.content
import io
from PIL import Image

image1=Image.open(io.BytesIO(image))
image1.show()
#image1.save('C:/Users/User/Documents/My Tableau Repository/Shapes/MyImages/image1.png')

import boto3
s3 = boto3.resource('s3')

# Upload the file
# change `image.png` to whatever you want the file to be called

s3.Object('di-statefarm', 'analytics/image_ceo.png').put(ACL="public-read", ContentDisposition="inline", ContentType="image/png", Body=open('C:/Users/User/Documents/My Tableau Repository/Shapes/MyImages/image_ceo.png', 'rb'))