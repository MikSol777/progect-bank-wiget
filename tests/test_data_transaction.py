from src.data_transaction import count_operations_by_category, sort_transaction


def test_sort_transaction_with_match():
    transactions = [
        {"id": 1, "description": "Payment for services", "amount": 100},
        {"id": 2, "description": "Refund for item", "amount": 50},
        {"id": 3, "description": "Payment for goods", "amount": 200},
    ]

    result = sort_transaction(transactions, "payment")

    assert len(result) == 2
    assert result[0]["description"] == "Payment for services"
    assert result[1]["description"] == "Payment for goods"


def test_sort_transaction_without_match():
    transactions = [
        {"id": 1, "description": "Payment for services", "amount": 100},
        {"id": 2, "description": "Refund for item", "amount": 50},
        {"id": 3, "description": "Payment for goods", "amount": 200},
    ]

    result = sort_transaction(transactions, "transfer")

    assert len(result) == 0


def test_sort_transaction_empty_list():
    transactions = []

    result = sort_transaction(transactions, "payment")

    assert len(result) == 0


def test_count_operations_by_category_with_matching_categories():
    transactions = [
        {"id": 1, "description": "Payment for services", "amount": 100},
        {"id": 2, "description": "Refund for item", "amount": 50},
        {"id": 3, "description": "Payment for goods", "amount": 200},
        {"id": 4, "description": "Payment for services", "amount": 300},
    ]
    categories = ["payment", "refund"]

    result = count_operations_by_category(transactions, categories)

    assert result == {"payment": 3, "refund": 1}


def test_count_operations_by_category_case_insensitive():
    transactions = [
        {"id": 1, "description": "Payment for services", "amount": 100},
        {"id": 2, "description": "Refund for item", "amount": 50},
        {"id": 3, "description": "payment for goods", "amount": 200},
    ]
    categories = ["Payment", "refund"]

    result = count_operations_by_category(transactions, categories)

    assert result == {"Payment": 2, "refund": 1}


def test_count_operations_by_category_empty_categories():
    transactions = [
        {"id": 1, "description": "Payment for services", "amount": 100},
        {"id": 2, "description": "Refund for item", "amount": 50},
    ]
    categories = []

    result = count_operations_by_category(transactions, categories)

    assert result == {}
