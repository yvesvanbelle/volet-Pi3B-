#  MIT License
#  Copyright 2019 Yves Van Belle

import datetime
import time

light = 0  # It is dark
temp_humidity = (23, 40)
start_evening = datetime.time(17)
start_morning = datetime.time(6, 30)
current_time = datetime.datetime.now().time()
current_day = datetime.datetime.now().weekday()  # 0 is monday

with open('statusvolet.txt', 'r') as f:
    status = f.read()

action = "Bubendorff volet up"

if(light == 0):  # if it is dark
    if(start_evening < current_time < start_morning):  # if it is between 17:00 and 6:30
        if(current_day < 5):  # if current day is before saturday
            action = ("Bubendorff volet down")

if(temp_humidity[0] > 24):  # if temp is higher than 24°C
    action = ("Bubendorff volet down")

if(action == status):
    print('No action')
else:
    with open('statusvolet.txt', 'w') as f:
        f.write(action)
        print(action)
