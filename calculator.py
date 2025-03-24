print("Basic Calculator:")


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Math Error"
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Get user input safely
input1 = get_number("Enter first number: ")
input2 = get_number("Enter second number: ")
operator = input("Enter the operator (+, -, *, /): ")

# Perform the operation
if operator == '+':
    result = add(input1, input2)
elif operator == '-':
    result = subtract(input1, input2)
elif operator == '*':
    result = multiply(input1, input2)
elif operator == '/':
    result = divide(input1, input2)
else:
    result = "Invalid operator"

# Display result
print("Result:", result)
