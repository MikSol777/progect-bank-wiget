import pytest

from src.generators import filter_by_currency, transaction_descriptions,  card_number_generator

def test_filter_by_currency(list_transactions):
    assert next(filter_by_currency(list_transactions, "USD")) == {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
    assert next(filter_by_currency(list_transactions, "RUB")) == {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }

def test_transaction_descriptions(list_transactions):
        assert next(transaction_descriptions(list_transactions)) == "Перевод организации"

def test_card_number_generator():
    number_card = card_number_generator(1, 3)
    assert next(number_card) == "0000 0000 0000 0001"
    assert next(number_card) == "0000 0000 0000 0002"
    assert next(number_card) == "0000 0000 0000 0003"