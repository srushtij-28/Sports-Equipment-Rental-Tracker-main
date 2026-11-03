import json
import os

from config import DATA_DIR, EQUIPMENT_FILE, RENTALS_FILE


def initialize_storage():
    os.makedirs(DATA_DIR, exist_ok=True)

    for file_path in [EQUIPMENT_FILE, RENTALS_FILE]:
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump([], file, indent=4)


def load_json(file_path):
    initialize_storage()

    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_json(file_path, data):
    initialize_storage()

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def load_equipment():
    return load_json(EQUIPMENT_FILE)


def save_equipment(equipment):
    save_json(EQUIPMENT_FILE, equipment)


def load_rentals():
    return load_json(RENTALS_FILE)


def save_rentals(rentals):
    save_json(RENTALS_FILE, rentals)
