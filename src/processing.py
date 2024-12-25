def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    new_list_dict = []
    for i in list_dict:
        for value in i.values():
            if value == state:
                new_list_dict.append(i)
    return new_list_dict

def sort_by_date(list_dict: list[dict], data: bool = True ) -> list[dict]:
    sort_list_by_data = sorted(list_dict, key=lambda x: x['date'],reverse = data)
    return sort_list_by_data
