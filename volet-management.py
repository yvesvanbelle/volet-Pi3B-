#  MIT LIcense
#  Copyright 2019 Yves Van Belle

from bubendorfftest import *


if is_dark(PIN_LIGHT) is True:
    relais_down
else:
    relais_up

print(temp_humidity_inside()[0])
print(temp_humidity_outside()[0])
