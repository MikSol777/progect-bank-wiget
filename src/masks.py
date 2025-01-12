def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""
    if len(card_number) != 16 or card_number.isdigit() == False:
        raise ValueError("Неверный ввод номера карты")
    card_mask = [i for i in str(card_number)]
    return f"{"".join(card_mask[:4])} {"".join(card_mask[4:6])}** **** {"".join(card_mask[-4:])}"


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску."""
    if len(account_number) != 20 or account_number.isdigit() == False:
        raise ValueError("Неверный ввод номера счета")
    mask_account = [i for i in str(account_number)]
    return f"**{"".join(mask_account[-4:])}"
