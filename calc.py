# A simple calculator that can add, subtract, multiply and divide
from operator import truediv, mul, add, sub


operators = {"+": add, "-": sub, "*": mul, "/": truediv}


def calculate(s):
    if s.isdigit():
        return int(s)  # Convert a digit string to int

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
            """
            Here we're recursively calculating left and right till they become integers.
            Our goal is to get this kind of expression in the end:
            add(1, 6)
            """


def inform():
    ready_to_quit = False

    while not ready_to_quit:
        calc = input(
            "\nThis calculator supports add, sub, mul and div operations. Enter below, what you want to calculate or type 'q' to quit:\n"
        )

        if calc.lower() == "q":
            ready_to_quit = True
            print("See you later.")
        else:
            print("Answer: " + str(calculate(calc)))


inform()
