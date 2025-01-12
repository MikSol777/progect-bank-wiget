import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_type_number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_account_card(card_type_number, expected):
    assert mask_account_card(card_type_number) == expected


def test_get_date(date):
    assert get_date("2024-03-11T02:26:18.671407") == date


def test_date_len_error():
    with pytest.raises(ValueError) as exc_info:
        get_date("20241-03-11T02:26:18.671407")
    with pytest.raises(ValueError) as exc_info:
        get_date("202l-as-11T02:26:18.671407")
    with pytest.raises(ValueError) as exc_info:
        get_date("2024-03-41T02:26:18.671407")
