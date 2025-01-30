import requests


def Exchange_api(to_currency, from_currency, amount, api_key):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

    payload = {}
    headers= {"apikey": api_key}

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    if status_code == 200:
        result = response.json()
        return result.get("result")
    if amount == 0:
        return 0
    else:
        return print("Ошибка при запросе:", response.text)