from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_type_number: str) -> str:
    """Возвращает строку с замаскированным номером"""
    list_card = card_type_number.rsplit(maxsplit=1)
    if "Счет" in card_type_number:
        return f"{list_card[0]} {get_mask_account(list_card[1])}"
    else:
        return f"{list_card[0]} {get_mask_card_number(list_card[1])}"


def get_date(date: str) -> str:
    """возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    list_date = date.split("-")
    return f"{list_date[2][:2]}.{list_date[1]}.{list_date[0]}"
