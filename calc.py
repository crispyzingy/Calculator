# A simple calculator that can add, subtract, multiply and divide


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


print("Select operation:")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Division\n")

# Ask choice of the user
choice = input("Enter choice(1/2/3/4): ")

if choice in ("1", "2", "3", "4"):
    # Take input from user
    x = float(input("\nFirst Number: "))
    y = float(input("Second Number: "))

    if choice == "1":
        print(f"\n{x} + {y} = {calc(add, x, y)}")

    elif choice == "2":
        print(f"\n{x} - {y} = {calc(sub, x, y)}")

    elif choice == "3":
        print(f"\n{x} * {y} = {calc(mul, x, y)}")

    elif choice == "4":
        print(f"\n{x} / {y} = {calc(div, x, y)}")

else:
    print("\nInvalid Input")
