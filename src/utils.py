import json
import logging
import os

log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file_path = os.path.join(log_directory, "utils.log")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s")
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(log_file_path, mode="w")
stream_handler.setFormatter(log_formatter)
file_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


def path_to_json(path):
    """принимает на вход путь до JSON-файла (../data/operations.json) и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    try:
        with open(path, "rb") as file:
            data = json.load(file)
        if list(data):
            logger.info("Успешно загружены данные")
            return data
        else:
            logger.warning("Файл не содержит список. Возвращается пустой список.")
            return []
    except FileNotFoundError:
        logger.error("Файл по пути не найден.")
        return []
    except json.JSONDecodeError:
        logger.error("Ошибка при чтении JSON в файле . Возможно, файл поврежден.")
        return []
