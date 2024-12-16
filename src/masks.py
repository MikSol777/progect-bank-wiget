def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    card_mask = [i for i in str(card_number)]
    return f"{"".join(card_mask[:4])} {"".join(card_mask[4:6])}** **** {"".join(card_mask[12:])}"


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    mask_account = [i for i in str(account_number)]
    return f"**{"".join(mask_account[16:])}"
