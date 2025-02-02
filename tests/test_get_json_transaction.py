from unittest.mock import patch, Mock
from src.external_api import get_json_transaction


def test_get_json_transaction_rub():
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "RUB"}
        }
    }

    result = get_json_transaction(transaction)
    assert result == 100.0


def test_get_json_transaction_usd_success():
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 7500}  # Пример конвертированной суммы в рублях

    with patch("requests.request", return_value=mock_response):
        result = get_json_transaction(transaction)
        assert result == 7500


def test_get_json_transaction_eur_success():
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "EUR"}
        }
    }

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 8500}

    with patch("requests.request", return_value=mock_response):
        result = get_json_transaction(transaction)
        assert result == 8500


def test_get_json_transaction_usd_error():
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"

    with patch("requests.request", return_value=mock_response):
        result = get_json_transaction(transaction)
        assert result == "Ошибка при запросе курса для USD: Internal Server Error"


def test_get_json_transaction_eur_error():
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "EUR"}
        }
    }

    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"

    with patch("requests.request", return_value=mock_response):
        result = get_json_transaction(transaction)
        assert result == "Ошибка при запросе курса для EUR: Internal Server Error"


def test_get_json_transaction_unknown_currency():
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "JPY"}
        }
    }

    result = get_json_transaction(transaction)
    assert result == "Неизвестная валюта"


def test_get_json_transaction_missing_amount():
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {}
    }

    result = get_json_transaction(transaction)
    assert result == "Ошибка: Нет данных о сумме транзакции"



def test_get_json_transaction_missing_operation_amount():
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",

    }

    result = get_json_transaction(transaction)
    assert result == "Ошибка: Нет данных о сумме транзакции"
