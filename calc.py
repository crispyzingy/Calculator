# A simple calculator that can add, subtract, multiply and divide
from operator import truediv, mul, add, sub


operators = {"+": add, "-": sub, "*": mul, "/": truediv}


def calculate(s):
    if s.isdigit():
        return float(s)  # Convert a digit string to float
    for char in operators.keys():  # 1 + 2 * 3
        left, operator, right = s.partition(char)
        """
        Partitions like:
        left = '1'
        operator = '+'
        right = '2*3'
        """
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))
            """Here we, re recursively calculating left and right till they become floats. Our goal is to get this kind of expression in the end: add(1, 6)"""


def want_to_continue():
    calc_again = input(
        "Do you want to calculate again? Please type Y for YES or N for NO.\n"
    )
    if calc_again.lower() == "y":
        inform()
    elif calc_again.lower() == "n":
        print("See you later.")
    else:
        want_to_continue()


def inform():
    calc = input(
        "\nThis calculator supports add, sub, mul and div operations. Enter, what you want to calculate:\n"
    )
    print("Answer: " + str(calculate(calc)))


inform()
want_to_continue()
