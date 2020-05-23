# A simple calculator that can add, subtract, multiply and divide
import sys


def calc(f, x, y):
    return f(x, y)


# adds two numbers
def add(x, y):
    return x + y


# subtracts two numbers
def sub(x, y):
    return x - y


# subtracts two numbers
def mul(x, y):
    return x * y


# subtracts two numbers
def div(x, y):
    return x / y


def again():
    calc_again = input(
        "Do you want to calculate again? Please type Y for YES or N for NO. "
    )
    if calc_again.lower() == "y":
        calculate()
    elif calc_again.lower() == "n":
        print("See you later.")
    else:
        again()


def calculate():
    choices = ["1", "2", "3", "4"]
    choice = "0"  # initiation
    ready_to_quit = False
    while not ready_to_quit and choice not in choices:
        print("What would you like to do?")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit\n")

        # Ask choice of the user
        choice = input("Enter choice (1/2/3/4/5) and press enter: ")

        if choice in choices:
            # Take input from user
            x = float(input("\nFirst Number: "))
            y = float(input("Second Number: "))

            if choice == "1":
                print(f"\n{x} + {y} = {calc(add, x, y)}\n")

            elif choice == "2":
                print(f"\n{x} - {y} = {calc(sub, x, y)}\n")

            elif choice == "3":
                print(f"\n{x} * {y} = {calc(mul, x, y)}\n")

            elif choice == "4":
                print(f"\n{x} / {y} = {calc(div, x, y)}\n")

        elif choice == "5":
            ready_to_quit = True
            sys.exit("See you later!")

        again()


calculate()
