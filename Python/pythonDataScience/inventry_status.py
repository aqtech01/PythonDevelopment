def inventory_status(current_quantity, reorder_level, reorder_quantity, unit_cost):
    if current_quantity < reorder_level:
        quantity_needed = reorder_level - current_quantity
        print("\nStatus: Below the Reorder Level")
        print(f"Quantity needed to reach reorder level: {quantity_needed}")
        # Reorder is essential to gain reorder level
        print("\nReorder is Required: Yes")
        reorder_decision = input("Do you want to place the Reorder? (yes/no): ").lower()
        if reorder_decision == "yes":
            total_quantity_reorder = quantity_needed + reorder_quantity
            total_cost = unit_cost * total_quantity_reorder
            print(f"Total quantity required to reach Reorder Level: {total_quantity_reorder}")
            print(f"Cost per unit: ${unit_cost:.2f}")
            print(f"Total Cost to reach Reorder Level: ${total_cost:.2f}")
            confirmation = input("Confirm Reorder? (yes/no): ").lower()
            if confirmation == "yes":
                print("Reorder Placed Successfully")
            else:
                print("Reorder Canceled")
    else:
        print("No Reorder Required: Inventory is Sufficient")
    # Returning the updated values might not be necessary in this context
    return current_quantity, reorder_level, reorder_quantity, unit_cost


def main():
    try:
        current_quantity = int(input("Enter the current quantity in stock: "))
        reorder_level = int(input("Enter the Reorder Level: "))
        reorder_quantity = int(input("Enter the Reorder Quantity: "))
        unit_cost = float(input("Enter the Cost per Unit: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    current_quantity, reorder_level, reorder_quantity, unit_cost = inventory_status(current_quantity, reorder_level,
                                                                                    reorder_quantity, unit_cost)


if __name__ == "__main__":
    main()
