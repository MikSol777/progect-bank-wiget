def filter_by_currency(transactions, currency):
    """Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)
    """
    new_list_transactions = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions))
    return iter(new_list_transactions)


def transaction_descriptions(transactions):
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start, stop):
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    for number in range(start, stop + 1):
        format_number = f"{number:016d}"
        yield f"{format_number[:4]} {format_number[4:8]} {format_number[8:12]} {format_number[12:16]}"
