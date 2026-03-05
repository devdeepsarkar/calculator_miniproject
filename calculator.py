import math

# Square root function
def square_root(x):
    if x < 0:
        raise ValueError("Negative number not allowed")
    return math.sqrt(x)

# Factorial function
def factorial(x):
    if x < 0:
        raise ValueError("Enter valid number")
    if isinstance(x, float) and not x.is_integer():
        raise ValueError("Enter valid number")
    return math.factorial(int(x))

# Natural logarithm
def natural_log(x):
    if x <= 0:
        raise ValueError("Log undefined")
    return math.log(x)

# Power function 
def power(x, b):
    return math.pow(x, b)


if __name__ == "__main__":
    while True:
        print("\nScientific Calculator")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Natural Log")
        print("4. Power")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            x = float(input("Enter number: "))
            print(square_root(x))

        elif choice == 2:
            x = float(input("Enter number: "))
            print(factorial(x))

        elif choice == 3:
            x = float(input("Enter number: "))
            print(natural_log(x))

        elif choice == 4:
            x = float(input("Enter base: "))
            b = float(input("Enter power: "))
            print(power(x, b))

        elif choice == 5:
            break