import json
from pathlib import Path


class DataLoader:
    def __init__(self):
        data_file = Path(__file__).parent / "test_data.json"
        with open(data_file) as f:
            self._data = json.load(f)

    def get_user(self, key: str) -> dict:
        return self._data["users"][key]
