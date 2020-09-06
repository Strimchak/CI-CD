import requests
from lib.Settings import URL_COVID

covid = requests.get(URL)
covid = covid.json()['Countries']
