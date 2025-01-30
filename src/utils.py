import json
import os
from dotenv import load_dotenv


from src.external_api import Exchange_api


def path_to_json(path):
    try:
        with open(path, 'rb') as file:
            data = json.load(file)
        return data
    except Exception:
        return []


def get_json_transaction(transactions):
    usd_sum = sum([float(i["operationAmount"]["amount"]) for i in transactions if i.get("operationAmount") and i["operationAmount"]["currency"]["code"] == "USD"])
    eur_sum = sum([float(i["operationAmount"]["amount"]) for i in transactions if i.get("operationAmount") and i["operationAmount"]["currency"]["code"] == "EUR"])
    rub_sum = sum([float(i["operationAmount"]["amount"]) for i in transactions if i.get("operationAmount") and i["operationAmount"]["currency"]["code"] == "RUB"])

    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    convert_usd = Exchange_api("RUB", "USD", usd_sum, API_KEY)
    convert_eur = Exchange_api("RUB", "EUR", eur_sum, API_KEY)

    return rub_sum + convert_usd + convert_eur

print(get_json_transaction(path_to_json("../data/operations.json")))
