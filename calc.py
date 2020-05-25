# A simple calculator that can add, subtract, multiply and divide


def calculate():
    # Take input from user
    print("Press Enter Key after giving your input")

    num1 = float(input("First Number:\n"))
    operator = input("Operator (+, -, *, /):\n")
    num2 = float(input("Second Number:\n"))

    if operator == "+":
        out = num1 + num2
    elif operator == "-":
        out = num1 - num2
    elif operator == "*":
        out = num1 * num2
    elif operator == "/":
        out = num1 / num2

    print(f"Answer: {out}")

    again()


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


calculate()
