# A simple calculator that can add, subtract, multiply and divide
from operator import truediv, mul, add, sub


operators = {"+": add, "-": sub, "*": mul, "/": truediv}


def calculate(s):
    if s.isdigit():
        return float(s)
    for char in operators.keys():
        left, operator, right = s.partition(char)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))


def want_to_continue():
    calc_again = input(
        "Do you want to calculate again? Please type Y for YES or N for NO. "
    )
    if calc_again.lower() == "y":
        inform()
    elif calc_again.lower() == "n":
        print("See you later.")
    else:
        want_to_continue()


def inform():
    calc = input(
        "This calculator supports add, sub, mul and div operations. Enter, what you want to calculate:\n"
    )
    print("Answer: " + str(calculate(calc)))


inform()
want_to_continue()
