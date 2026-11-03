from storage import load_equipment, load_rentals


def show_report():
    equipment = load_equipment()
    rentals = load_rentals()

    total_equipment = len(equipment)

    total_quantity = sum(
        item["quantity"] for item in equipment
    )

    available_quantity = sum(
        item["available"] for item in equipment
    )

    active_rentals = sum(
        1 for rental in rentals
        if rental["status"] == "Rented"
    )

    returned_rentals = sum(
        1 for rental in rentals
        if rental["status"] == "Returned"
    )

    total_rental_charges = sum(
        rental["rental_charge"] for rental in rentals
    )

    print("\n========== RENTAL REPORT ==========")
    print(f"Equipment Types    : {total_equipment}")
    print(f"Total Quantity     : {total_quantity}")
    print(f"Available Quantity : {available_quantity}")
    print(f"Active Rentals     : {active_rentals}")
    print(f"Returned Rentals   : {returned_rentals}")
    print("----------------------------------")
    print(f"Rental Charges     : Rs. {total_rental_charges:.2f}")
    print("==================================")
