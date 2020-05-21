# A simple calculator that can add, subtract, multiply and divide


def calc(f, x, y):
    return f(x, y)


# adds two numbers
def add(x, y):
    return x + y


# subtracts two numbers
def sub(x, y):
    return x - y


print("Select operation:")
print("1. Addition")
print("2. Subtract")

# Ask choice of the user
choice = input("Enter choice(1/2): ")

# Take input from user
x = float(input("Enter First Number: "))
y = float(input("Enter Second Number: "))

if choice == 1:
    print(f"{x} + {y} = {calc(add, x, y)}")

elif choice == 2:
    print(f"{x} - {y} = {calc(sub, x, y)}")

else:
    print("Invalid Input")
