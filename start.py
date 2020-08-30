import requests
URL_PB_API = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"


def get_data(URL):
    responce = requests.get(URL_PB_API)
    data = responce.json()
    return data


def show_currency(currencies):
    for x in currencies:
        print('{0:<5} {1:<3} {2:<2} {3:<4} {4:<10} {5:<4}{6:<0}'.format(
            x["ccy"], "-", x["base_ccy"], " ", x["buy"], x["sale"], "\n"))


currencies = get_data(URL_PB_API)

show_currency(currencies)
