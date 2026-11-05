
print("================================")
print("       MY CALCULATOR")
print("================================")
print("Welcome to Python Calculator!")


# Function for Addition
def add(a, b):
    return a + b


# Function for Subtraction
def subtract(a, b):
    return a - b


# Function for Multiplication
def multiply(a, b):
    return a * b


# Function for Division
def divide(a, b):
    return a / b


# Main Calculator Program
while True:

    print("\n===== CALCULATOR MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Exit option
    if choice == "5":
        print("Thank you for using the calculator!")
        break

    # Check valid operation
    elif choice in ["1", "2", "3", "4"]:

        # Take numbers from user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        # Perform selected operation
        if choice == "1":
            print("Result:", add(num1, num2))

        elif choice == "2":
            print("Result:", subtract(num1, num2))

        elif choice == "3":
            print("Result:", multiply(num1, num2))

        elif choice == "4":
            if num2 == 0:
                print("Error! Cannot divide by zero.")
            else:
                print("Result:", divide(num1, num2))

    else:
        print("Invalid choice! Please try again.")
