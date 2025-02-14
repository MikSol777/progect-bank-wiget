import re
from collections import defaultdict


def sort_transaction(transactions: list[dict], re_search: str) -> list[dict]:
    """принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка."""
    get_transactions = []
    pattern = re.compile(re_search, re.IGNORECASE)
    for transaction in transactions:
        for key, value in transaction.items():
            if re.search(pattern, str(key)) or re.search(pattern, str(value)):
                get_transactions.append(transaction)
                break
    return get_transactions


def count_operations_by_category(transactions_list: list[dict], categories: list[str]) -> dict[str, int]:
    """принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""
    category_count = defaultdict(int)
    for transaction in transactions_list:
        description = transaction.get("description", "").lower()
        for category in categories:
            if re.search(re.escape(category.lower()), description):
                category_count[category] += 1
    return dict(category_count)
