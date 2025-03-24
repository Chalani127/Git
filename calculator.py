from functions import add, subtract, multiply, divide, get_number

print("Basic Calculator:")

from functions import add, subtract, multiply, divide, get_number

def main():
    while True:
        # Getting user input 
        input1 = get_number("Enter first number: ")
        input2 = get_number("Enter second number: ")
        operator = input("Enter the operator or 'q' to quit: ")

        # Exit condition
        if operator.lower() == 'q':
            print("Exiting the calculator.")
            break

        # Perform the operation based on operator
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

        # Save calculation history to a file
        with open("calculation_history.txt", "a") as file:
            file.write(f"{input1} {operator} {input2} = {result}\n")

        # Display the result
        print("Result:", result)


if __name__ == "__main__":  
    main()

