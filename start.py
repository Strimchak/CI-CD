from Currency import Currency
from Covid19 import Covid
import time

import requests


currency = Currency()
covid = Covid()

counter = 0
while True:
    counter += 1
    print("Get online data => ", counter, " times")
    currency.start()
    time.sleep(300)


while True:
    covid.start()
    time.sleep(300)
