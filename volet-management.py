#  MIT License
#  Copyright 2019 Yves Van Belle

import time
from bubendorfftest import temp_humidity_inside, temp_humidity_outside, \
                           volet_down, volet_up, is_dark


volet_action = volet_up
volet_status = volet_action

while True:
    dark = is_dark()
    temp_in = temp_humidity_inside()[0]
    temp_out = temp_humidity_outside()[0]
    print('------')
    print('Temp_in:{}-Temp_out:{}-Is dark:{}'.format(temp_in, temp_out, dark))

    if dark is True:
        volet_action = volet_down
    elif (temp_in > 22) and (temp_out > temp_in):
        volet_action = volet_down
    else:
        volet_action = volet_up

    if volet_status != volet_action:
        volet_action()
        volet_status = volet_action

    time.sleep(3)  # 1/2 hour = 1800 seconds # 1 hour = 3600 seconds
