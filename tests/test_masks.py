from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number(number):
    assert get_mask_card_number("7000792289606361") == number


def test_mask_account(mask_account):
    assert get_mask_account("73654108430135874305") == mask_account
