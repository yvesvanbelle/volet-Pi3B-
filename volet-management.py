#  MIT LIcense
#  Copyright 2019 Yves Van Belle

from bubendorfftest import *

volet_action = volet_up


temp_in = temp_humidity_inside()[0]
temp_out = temp_humidity_outside()[0]

if (temp_in > 22) and (temp_out > temp_in):
    volet_action = volet_down

if is_dark() is True:
    volet_action = volet_down

volet_action()
