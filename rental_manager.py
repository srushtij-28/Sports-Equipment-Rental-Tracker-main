from datetime import date, datetime

from storage import (
    load_equipment,
    save_equipment,
    load_rentals,
    save_rentals
)

from utils import (
    get_next_id,
    input_required,
    input_integer,
    input_date,
    display_rental
)


def rent_equipment():
    equipment = load_equipment()

    if not equipment:
        print("No equipment has been registered.")
        return

    print("\n--- AVAILABLE EQUIPMENT ---")

    for item in equipment:
        print(
            f"{item['id']}. {item['name']} "
            f"(Available: {item['available']})"
        )

    try:
        equipment_id = int(input("Enter equipment ID: "))
    except ValueError:
        print("Enter a valid equipment ID.")
        return

    item = next(
        (item for item in equipment if item["id"] == equipment_id),
        None
    )

    if not item:
        print("Equipment not found.")
        return

    quantity = input_integer("Enter rental quantity: ", minimum=1)

    if quantity > item["available"]:
        print("Not enough equipment available.")
        return

    customer = input_required("Enter customer name: ")
    rental_date = input_date("Enter rental date (YYYY-MM-DD): ")
    due_date = input_date("Enter due date (YYYY-MM-DD): ")

    rental_start = datetime.strptime(rental_date, "%Y-%m-%d").date()
    rental_end = datetime.strptime(due_date, "%Y-%m-%d").date()

    if rental_end < rental_start:
        print("Due date cannot be before rental date.")
        return

    rental_days = (rental_end - rental_start).days + 1
    rental_charge = round(
        item["daily_rent"] * quantity * rental_days,
        2
    )

    rentals = load_rentals()

    rental = {
        "id": get_next_id(rentals),
        "equipment_id": item["id"],
        "equipment_name": item["name"],
        "customer": customer,
        "quantity": quantity,
        "rental_date": rental_date,
        "due_date": due_date,
        "return_date": None,
        "rental_charge": rental_charge,
        "status": "Rented"
    }

    item["available"] -= quantity

    rentals.append(rental)

    save_equipment(equipment)
    save_rentals(rentals)

    print("\nEquipment rented successfully!")
    print(f"Rental charge: Rs. {rental_charge:.2f}")


def return_equipment():
    rentals = load_rentals()
    equipment = load_equipment()

    try:
        rental_id = int(input("Enter rental ID: "))
    except ValueError:
        print("Enter a valid rental ID.")
        return

    rental = next(
        (
            record for record in rentals
            if record["id"] == rental_id
        ),
        None
    )

    if not rental:
        print("Rental record not found.")
        return

    if rental["status"] == "Returned":
        print("This equipment has already been returned.")
        return

    return_date = input_date("Enter return date (YYYY-MM-DD): ")

    rental_start = datetime.strptime(
        rental["rental_date"], "%Y-%m-%d"
    ).date()

    return_day = datetime.strptime(
        return_date, "%Y-%m-%d"
    ).date()

    if return_day < rental_start:
        print("Return date cannot be before the rental date.")
        return

    item = next(
        (
            item for item in equipment
            if item["id"] == rental["equipment_id"]
        ),
        None
    )

    if not item:
        print("Equipment record not found.")
        return

    rental["return_date"] = return_date
    rental["status"] = "Returned"

    item["available"] += rental["quantity"]

    save_equipment(equipment)
    save_rentals(rentals)

    print("Equipment returned successfully!")


def view_rentals():
    rentals = load_rentals()

    if not rentals:
        print("\nNo rental records found.")
        return

    print("\n--- RENTAL RECORDS ---")

    for rental in rentals:
        display_rental(rental)


def view_overdue_rentals():
    rentals = load_rentals()
    today = date.today()

    overdue = [
        rental for rental in rentals
        if rental["status"] == "Rented"
        and date.fromisoformat(rental["due_date"]) < today
    ]

    if not overdue:
        print("\nNo overdue rentals.")
        return

    print("\n--- OVERDUE RENTALS ---")

    for rental in overdue:
        display_rental(rental)
