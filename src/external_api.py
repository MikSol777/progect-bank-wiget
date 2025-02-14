import os

import requests
from dotenv import load_dotenv


def get_json_transaction(transaction):
    """Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float"""
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not transaction.get("operationAmount"):
        return "Ошибка: Нет данных о сумме транзакции"

    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return float(amount)
    elif currency in ["USD", "EUR"]:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.request("GET", url, headers=headers)

        if response.status_code == 200:
            json_result = response.json()
            currency_amount = json_result["result"]
            return currency_amount
        else:
            return f"Ошибка при запросе курса для {currency}: {response.text}"
    else:
        return "Неизвестная валюта"
