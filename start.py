from lib.Currency import Currency
from lib.Covid19 import Covid
import time

import requests


currency = Currency()
covid = Covid()
covid.start()

# counter = 0
# while True:
#     counter += 1
#     print("Get online data => ", counter, " times")
#     covid.start()
#     currency.start()
#     time.sleep(300)
