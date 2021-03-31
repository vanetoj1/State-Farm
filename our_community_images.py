# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 11:42:50 2021

@author: Vania Todorova
"""


from __future__ import print_function

import requests

from requests.auth import HTTPBasicAuth
import datetime 
from datetime import datetime, timedelta



today = datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-7] 

headers = {"Content-Type": "image/png","MAC":"80:1F:12:76:4B:E2" }

response = requests.get('http://192.168.254.20/api/maps/startstop/export?&from=2020-05-15T09:00:00&to={}'.format(today), headers=headers,auth=HTTPBasicAuth('Admin', 'dimin3421'))
                        
image = response.content
import io
from PIL import Image

image2 = Image.open(io.BytesIO(image))
image2.show()
#image2.save('C:/Users/User/Documents/My Tableau Repository/Shapes/MyImages/our_community.png')

#crop if needed
newsize = (570, 250) 
im1123456 = image2.resize(newsize) 
# Shows the image in image viewer  
im1123456.show()
im1123456.save('C:/Users/User/Documents/My Tableau Repository/Shapes/MyImages/our_community.png')

#upload to S3
import boto3
s3 = boto3.resource('s3')

# Upload the file
# change `image.png` to whatever you want the file to be called

s3.Object('di-statefarm', 'analytics/our_community.png').put(ACL="public-read", ContentDisposition="inline", ContentType="image/png", Body=open('C:/Users/User/Documents/My Tableau Repository/Shapes/MyImages/our_community.png', 'rb'))