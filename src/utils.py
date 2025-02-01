import json


def path_to_json(path):
    """принимает на вход путь до JSON-файла (../data/operations.json) и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(path, "rb") as file:
            data = json.load(file)
        return data
    except Exception:
        return []
