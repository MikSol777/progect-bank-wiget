from src.external_api import get_json_transaction
from unittest.mock import patch


@patch('requests.get')
def test_get_json_transaction(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 100.0}
    transactions = [
        {"operationAmount": {"amount": "10", "currency": {"code": "USD"}}},
        {"operationAmount": {"amount": "20", "currency": {"code": "EUR"}}},
        {"operationAmount": {"amount": "30", "currency": {"code": "RUB"}}}
    ]
    result = get_json_transaction(transactions)
    expected_result = 30 + 100 + 100
    assert result == expected_result

