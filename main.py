from src.masks import get_mask_card_number, get_mask_account
from src.utils import path_to_json


print(get_mask_card_number('1234567890123456'))
print(get_mask_card_number('1234'))
content = path_to_json('data/operations.json')
print(content[:1])
path_to_json('data/NOT_EXISTS.json')
print(get_mask_account("12312345645678978912"))