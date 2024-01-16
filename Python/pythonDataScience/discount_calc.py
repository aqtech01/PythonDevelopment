def discount_calc(quantity, unit_price):
    # print("ABC")
    original_cost = quantity * unit_price
    if quantity >= 50:
        discount_rate = 0.30
    elif quantity >= 20:
        discount_rate = 0.20
    elif quantity >= 10:
        discount_rate = 0.10
    else:
        discount_rate = 0.00

    discount_amount = original_cost * discount_rate
    final_cost = original_cost - discount_amount
    return original_cost, discount_rate, final_cost


def main():
    quantity = int(input("Enter your required quantity:- "))
    unit_price = int(input("Enter price of unit:- "))
    original_cost, discount_rate, final_cost = discount_calc(quantity, unit_price)
    print("\nOrder Summary:")
    print(f"Total Quantity: {quantity}")
    print(f"Price per Unit is : ${unit_price:.2f}")
    print(f"Discount on Products: ${discount_rate:.2f}")
    print(f"Original Cost is: ${original_cost:.2f}")
    print(f"Final Cost after Discount: ${final_cost:.2f}")


if __name__ == "__main__":
    main()
