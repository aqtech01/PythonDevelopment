def individual_sum_digit(i):
    sum_digit = 0

    while i > 0 and i >= 5:
        sum_digit = sum_digit + i % 10
        i = i // 10

    return sum_digit


def main():
    i = int(input("Enter your Number: "))

    i = individual_sum_digit(i)
    print(i)


if __name__ == "__main__":
    main()
