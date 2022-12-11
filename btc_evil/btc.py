import requests
import json
import time
import datetime

from filemanagement import *

key = getFromConfig('api_url')+getFromConfig('typeofcrypto')
print(key)
print(getFromConfig('difference'))

old_data = {'symbol': 'BTCUSDT', 'price': '0'}

while True:

    currentDate = datetime.datetime.now()
    date = {'year': currentDate.year,
            'month': currentDate.month,
            'day': currentDate.day,
            'hour': currentDate.hour,
            'minute': currentDate.minute,
            'second': currentDate.second
            }

    data = requests.get(key)  
    data = data.json()

    date["btcusdtprice"] = data['price']

    print(str(data['price']) + " <- current btc price oniichan "+ str(old_data['price'] + " <- old btc price oniichan"))

    if float(data['price']) - float(old_data['price']) >= float(getFromConfig('difference')) or float(data['price']) - float(old_data['price']) <= (float(getFromConfig('difference')) * -1):
        print(f"{data['symbol']} hello ev1lclow3n, the price is {data['price']}")
        writeFile(getFromConfig('dataFile'), str(date))

        old_data = data.copy()

    time.sleep(1)
