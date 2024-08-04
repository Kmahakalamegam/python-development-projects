def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculate():
    print("*** Select operation to perform: ***")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter  your choice (1/2/3/4): ")

    if operation in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Dictionary to simulate switch-case
        switch = {
            '1': add,
            '2': subtract,
            '3': multiply,
            '4':divide
        }

        # Get the function based on user choice
        func = switch.get(operation)

        # Call the function and print the result
        if func:
            result = func(num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid operation selected.")
    else:
        print("Invalid input! Please select a valid operation.")

# Run the calculator
calculate()
