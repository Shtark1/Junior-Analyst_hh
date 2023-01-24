import requests
import re
import datetime


all_coin = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "ATOM": "cosmos",
    "SOL": "solana",
    "XLM": "stellar",
}


# TODO: Получение информации о манете по API
def price_coin(coin_asset, date_from, date_to):
    date_days = []
    price_coin_from_to = []

    start = timestamp(date_from)
    end = timestamp(date_to)

    url = f"https://api.coincap.io/v2/assets/{all_coin[f'{coin_asset}']}/history?interval=d1&start={start}&end={end}"
    print(url)
    coin = requests.get(url).json()["data"]

    for price_and_date in coin:
        date = re.sub("T00:00:00.000Z", "", price_and_date["date"])
        price = round(float(price_and_date["priceUsd"]), 2)

        date_days.append(date)
        price_coin_from_to.append(price)

    return [date_days, price_coin_from_to]

# TODO: Перевод времени в мс
def timestamp(dt):
    epoch = datetime.datetime.strptime('01-01-70', '%d-%m-%y').date()
    return (dt - epoch).total_seconds() * 1000.0
