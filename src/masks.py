def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""
    card_mask = [i for i in str(card_number)]
    return f"{"".join(card_mask[:4])} {"".join(card_mask[4:6])}** **** {"".join(card_mask[-4:])}"


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску."""
    mask_account = [i for i in str(account_number)]
    return f"**{"".join(mask_account[-4:])}"
