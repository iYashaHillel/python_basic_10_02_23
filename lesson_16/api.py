import json
from typing import Optional

import requests

# RESTful API
# HTTP(s)

# url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
# resp = requests.get(url)
# currencies = resp.json()
#
# for currency in currencies:
#     print(f'CCY: {currency["ccy"]}\nBUY: {currency["buy"]}\n\n')
#
# resp = requests.get('https://google.com')
# print(resp.content)


def get_currency(date: str, currency_code: str) -> Optional[dict]:
    url = f'https://api.privatbank.ua/p24api/exchange_rates?date={date}'
    resp = requests.get(url, headers={
        'Authorization': 'Bearer {API_KEY}'
    })
    if not resp.ok:
        print(resp.text)
        return None
    currencies = resp.json()
    rates = currencies['exchangeRate']

    filtered_currencies = list(filter(lambda x: x['currency'].lower() == currency_code.lower(), rates))
    if len(filtered_currencies) == 0:
        print(f'Currency {currency_code} not found!')
        return None
    else:
        return filtered_currencies[0]


def main():
    while True:
        date = input('Enter date: ')
        currency = input('Enter currency code: ')
        currency = get_currency(date, currency)
        print(currency)


main()





