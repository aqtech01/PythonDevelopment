def grade_calc(marks):
    # print()

    aver = marks / 3

    if aver >= 90:
        res = "A"
    elif aver >= 80:
        res = "B"
    elif aver >= 70:
        res = "C"
    elif aver >= 60:
        res = "D"
    else:
        res = "F"
    return aver, res


def main():
    sum_marks = 0
    for i in range(3):
        enter_marks = int(input("Enter your marks:- "))
        sum_marks = enter_marks + sum_marks

    aver, res = grade_calc(sum_marks)
    print("\nCalculated Result ")
    print(f"Sum of marks is {sum_marks}")
    print(f"Average of marks is {aver}")
    print(f"Grade: {res}")


if __name__ == "__main__":
    main()
