import requests
import os
from dotenv import load_dotenv


def get_json_transaction(transactions):
    """принимает на вход транзакцию и возвращает сумму транзакций (amount) в рублях, тип данных — float"""
    usd_sum = sum(
        [
            float(i["operationAmount"]["amount"])
            for i in transactions
            if i.get("operationAmount") and i["operationAmount"]["currency"]["code"] == "USD"
        ]
    )
    eur_sum = sum(
        [
            float(i["operationAmount"]["amount"])
            for i in transactions
            if i.get("operationAmount") and i["operationAmount"]["currency"]["code"] == "EUR"
        ]
    )
    rub_sum = sum(
        [
            float(i["operationAmount"]["amount"])
            for i in transactions
            if i.get("operationAmount") and i["operationAmount"]["currency"]["code"] == "RUB"
        ]
    )

    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    url_usd = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={'USD'}&amount={usd_sum}"
    url_eur = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={'EUR'}&amount={eur_sum}"
    headers = {"apikey": API_KEY}

    convert_usd = 0
    convert_eur = 0

    if usd_sum > 0:
        response_usd = requests.get(url_usd, headers=headers)
        status_code_usd = response_usd.status_code
        if status_code_usd == 200:
            result = response_usd.json()
            convert_usd = result.get("result")
        else:
            print("Ошибка при запросе USD:", response_usd.text)

    if eur_sum > 0:
        response_eur = requests.get(url_eur, headers=headers)
        status_code_eur = response_eur.status_code
        if status_code_eur == 200:
            result = response_eur.json()
            convert_eur = result.get("result")
        else:
            print("Ошибка при запросе EUR:", response_eur.text)

    return rub_sum + convert_usd + convert_eur
