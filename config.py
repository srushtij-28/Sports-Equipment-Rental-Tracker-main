import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

EQUIPMENT_FILE = os.path.join(DATA_DIR, "equipment.json")
RENTALS_FILE = os.path.join(DATA_DIR, "rentals.json")

RENTAL_STATUSES = ["Rented", "Returned"]
