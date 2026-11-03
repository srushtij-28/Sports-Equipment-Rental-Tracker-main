from datetime import datetime


def get_next_id(records):
    if not records:
        return 1

    return max(record["id"] for record in records) + 1


def input_required(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")


def input_integer(message, minimum=0):
    while True:
        try:
            value = int(input(message))

            if value < minimum:
                print(f"Enter a number greater than or equal to {minimum}.")
                continue

            return value

        except ValueError:
            print("Enter a valid whole number.")


def input_amount(message):
    while True:
        try:
            value = float(input(message))

            if value < 0:
                print("Amount cannot be negative.")
                continue

            return round(value, 2)

        except ValueError:
            print("Enter a valid amount.")


def input_date(message):
    while True:
        value = input(message).strip()

        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Enter date in YYYY-MM-DD format.")


def display_equipment(item):
    print("-" * 60)
    print(f"ID              : {item['id']}")
    print(f"Equipment       : {item['name']}")
    print(f"Category        : {item['category']}")
    print(f"Total Quantity  : {item['quantity']}")
    print(f"Available       : {item['available']}")
    print(f"Daily Rent      : Rs. {item['daily_rent']:.2f}")


def display_rental(rental):
    print("-" * 60)
    print(f"Rental ID       : {rental['id']}")
    print(f"Equipment       : {rental['equipment_name']}")
    print(f"Customer        : {rental['customer']}")
    print(f"Quantity        : {rental['quantity']}")
    print(f"Rental Date     : {rental['rental_date']}")
    print(f"Due Date        : {rental['due_date']}")
    print(f"Return Date     : {rental['return_date'] or 'Not returned'}")
    print(f"Rental Charge   : Rs. {rental['rental_charge']:.2f}")
    print(f"Status          : {rental['status']}")
