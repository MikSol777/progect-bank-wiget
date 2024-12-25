def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    new_list_dict = []
    for i in list_dict:
        for value in i.values():
            if value == state:
                new_list_dict.append(i)
    return new_list_dict
