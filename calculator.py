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

# Get user input
input1 = float(input("Enter first number: "))
input2 = float(input("Enter second number: "))6
operator = input("Enter the operator: ")

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

print("Result:", result)