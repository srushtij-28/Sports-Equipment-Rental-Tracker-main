from storage import load_equipment, save_equipment
from utils import (
    get_next_id,
    input_required,
    input_integer,
    input_amount,
    display_equipment
)


def add_equipment():
    equipment = load_equipment()

    name = input_required("Enter equipment name: ")
    category = input_required("Enter category: ")
    quantity = input_integer("Enter quantity: ", minimum=1)
    daily_rent = input_amount("Enter daily rental charge: ")

    item = {
        "id": get_next_id(equipment),
        "name": name,
        "category": category,
        "quantity": quantity,
        "available": quantity,
        "daily_rent": daily_rent
    }

    equipment.append(item)
    save_equipment(equipment)

    print("\nEquipment added successfully!")


def view_equipment():
    equipment = load_equipment()

    if not equipment:
        print("\nNo equipment available.")
        return

    print("\n--- SPORTS EQUIPMENT ---")

    for item in equipment:
        display_equipment(item)


def search_equipment():
    equipment = load_equipment()

    keyword = input_required(
        "Enter equipment name to search: "
    ).lower()

    results = [
        item for item in equipment
        if keyword in item["name"].lower()
    ]

    if not results:
        print("No matching equipment found.")
        return

    for item in results:
        display_equipment(item)
