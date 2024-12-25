def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению"""
    new_list_dict = []
    for i in list_dict:
        for value in i.values():
            if value == state:
                new_list_dict.append(i)
    return new_list_dict


def sort_by_date(list_dict: list[dict], data: bool = True) -> list[dict]:
    """возвращает новый список, отсортированный по дате (date)"""
    sort_list_by_data = sorted(list_dict, key=lambda x: x["date"], reverse=data)
    return sort_list_by_data
