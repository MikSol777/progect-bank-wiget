import logging
import os

log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file_path = os.path.join(log_directory, "masks.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler(log_file_path, mode="w")],
)

logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""

    if len(card_number) != 16 or not card_number.isdigit():
        logger.error(f"Неверный ввод номера карты: {card_number}")
        return "Ошибка: Неверный ввод номера карты"

    card_mask = [i for i in str(card_number)]
    masked_card = f"{''.join(card_mask[:4])} {' '.join(card_mask[4:6])}** **** {''.join(card_mask[-4:])}"

    logger.info(f"Маскированный номер карты: {masked_card}")
    return masked_card


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску."""

    if len(account_number) != 20 or not account_number.isdigit():
        logger.error(f"Неверный ввод номера счета: {account_number}")
        return "Ошибка: Неверный ввод номера счета"

    mask_account = [i for i in str(account_number)]
    masked_account = f"**{''.join(mask_account[-4:])}"

    logger.info(f"Маскированный номер счета: {masked_account}")
    return masked_account
