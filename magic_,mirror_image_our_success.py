# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 09:13:56 2021

@author: User
"""


from __future__ import print_function

import requests

from requests.auth import HTTPBasicAuth
import datetime 
from datetime import datetime, timedelta



today = datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-7] 

headers = {"Content-Type": "image/png","MAC":"54:10:EC:B6:E6:E8" }

response = requests.get('http://192.168.254.14/api/maps/startstop/export?&from=2020-05-15T09:00:00&to={}'.format(today), headers=headers,auth=HTTPBasicAuth('Admin', 'dimin3421'))
                        
image = response.content
import io
from PIL import Image

image7 = Image.open(io.BytesIO(image))
image7.show()
#image7.save('C:/Users/User/Documents/My Tableau Repository/Shapes/MyImages/our_success.png')

#crop image and save in the tableau repo in the computer 
newsize = (570, 250) 
im112345 = image7.resize(newsize) 
# Shows the image in image viewer  
im112345.show()
im112345.save('C:/Users/User/Documents/My Tableau Repository/Shapes/MyImages/our_success.png')