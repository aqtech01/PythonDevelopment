def calculator(num1, num2, oper):
    if oper == "+":
        res = num1 + num2
    elif oper == "-":
        res = num1 + num2
    elif oper == "*":
        res = num1 + num2
    elif oper == "/":
        res = num1 + num2
    else:
        res = "Invalid Operation or value"
    return res


def main():
    print("\nEnter your values----")
    num1 = float(input("Enter First Value"))
    num2 = float(input("Enter Second Value"))
    print("\nEnter your Operation which should be + ,- , *, /")
    oper = input("Enter operation")
    calculated_value = calculator(num1, num2, oper)
    print(calculated_value)


if __name__ == "__main__":
    main()
