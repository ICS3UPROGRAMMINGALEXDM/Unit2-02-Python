#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 02//22
# Description: Calculates the area and perimeter of a rectangle with user input


def calculate():
    print("Make sure to enter numbers only!")
    while True:
        num1 = input("What is the height of your retangle? \n").strip()
        try:
            height = float(num1)
            break
        except ValueError:
            print("That isn't a number. Please try again")

    while True:
        num2 = input("What is the width of your rectangle?\n").strip()
        try:
            width = float(num2)
            break
        except ValueError:
            print("That isn't a number. Please try again")

    perimeter = (2 * height) + (2 * width)
    area = height * width

    print(
        "The perimeter of your rectangle is {:.2f} u. \nThe area of your rectangle is {:.2f} u^2!".format(
            perimeter, area
        )
    )


def main():
    calculate()


if __name__ == "__main__":
    main()
