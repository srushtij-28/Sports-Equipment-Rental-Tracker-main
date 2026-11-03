from storage import initialize_storage

from equipment_manager import (
    add_equipment,
    view_equipment,
    search_equipment
)

from rental_manager import (
    rent_equipment,
    return_equipment,
    view_rentals,
    view_overdue_rentals
)

from report_manager import show_report


def main():
    initialize_storage()

    while True:
        print("\n======================================")
        print("   SPORTS EQUIPMENT RENTAL TRACKER")
        print("======================================")

        print("1. Add Equipment")
        print("2. View Equipment")
        print("3. Search Equipment")
        print("4. Rent Equipment")
        print("5. Return Equipment")
        print("6. View Rental Records")
        print("7. View Overdue Rentals")
        print("8. View Reports")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_equipment()

        elif choice == "2":
            view_equipment()

        elif choice == "3":
            search_equipment()

        elif choice == "4":
            rent_equipment()

        elif choice == "5":
            return_equipment()

        elif choice == "6":
            view_rentals()

        elif choice == "7":
            view_overdue_rentals()

        elif choice == "8":
            show_report()

        elif choice == "9":
            print("\nThank you for using the tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
