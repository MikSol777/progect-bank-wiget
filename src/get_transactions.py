import pandas as pd


def get_csv(path_csv):
    """принимает на вход путь до csv-файла (../data/transactions.csv) и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    try:
        read_csv = pd.read_csv(path_csv, sep=";").to_dict(orient="records")
        if list(read_csv):
            return read_csv
        else:
            return []
    except FileNotFoundError:
        return []


def get_xlsx(path_excel):
    """принимает на вход путь до xlsx-файла (../data/transactions_excel.xlsx) и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    try:
        read_excel = pd.read_excel(path_excel).to_dict(orient="records")
        if list(read_excel):
            return read_excel
        else:
            return []
    except FileNotFoundError:
        return []
