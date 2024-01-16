def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        comment = "You are under weight"
    elif 18.5 >= bmi < 25:
        comment = "Your weight is normal"
    elif 25 >= bmi < 30:
        comment = "You are over weight"
    else:
        comment = "You are obese"

    return comment,bmi


def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in m: "))

    comment, bmi = bmi_calculator(weight, height)
    print(f"your BMI is {bmi:.2f} and you are classified as {comment} ")


if __name__ == "__main__":
    main()
