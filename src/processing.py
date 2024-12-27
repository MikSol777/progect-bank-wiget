def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению"""
    return [i for i in list_dict if i["state"] == state]


def sort_by_date(list_dict: list[dict], sort_date: bool = True) -> list[dict]:
    """возвращает новый список, отсортированный по дате (date)"""
    return sorted(list_dict, key=lambda x: x["date"], reverse=sort_date)
