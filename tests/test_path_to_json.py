from unittest.mock import mock_open, patch

from src.utils import path_to_json


def test_path_to_json():
    mock_file = mock_open(read_data='[{"id": 1, "amount": 100}]')
    with patch("builtins.open", mock_file):
        result = path_to_json("fake_path.json")
        assert result == [{"id": 1, "amount": 100}]

    mock_file = mock_open()
    mock_file.side_effect = FileNotFoundError
    with patch("builtins.open", mock_file):
        result = path_to_json("non_existent_file.json")
        assert result == []
