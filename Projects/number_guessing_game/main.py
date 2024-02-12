import random
import math


def select_range():
    lower_range = int(input("Enter Lower Range:- "))
    upper_range = int(input("Enter Upper Range:- "))
    x = random.randint(lower_range, upper_range)
    return x


def guess_number(x):
    count = 0
    while True:
        count += 1
        guess = int(input("Guess Your Number "))
        if guess > x:
            print("Too High")
        elif guess < x:
            print("Too Low")
        elif guess == x:
            print("You Guess")
            break
        else:
            print("Invalid input")
    print(f"Your Total attempt was {count}")


def main():
    x = select_range()
    guess_number(x)


if __name__ ==  "__main__":
    main()