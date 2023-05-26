def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Cannot divide by zero!")

def calculator(operation, x, y):
    match operation:
        case '+':
            result = add(x, y)
            print(f"{x} + {y} = {result}")
        case '-':
            result = subtract(x, y)
            print(f"{x} - {y} = {result}")
        case '*':
            result = multiply(x, y)
            print(f"{x} * {y} = {result}")
        case '/':
            result = divide(x, y)
            if result is not None:
                print(f"{x} / {y} = {result}")
        case _:
            print("Error: Invalid operation!")

# Main program loop
while True:
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '0':
        print("Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        calculator(choice, num1, num2)
    else:
        print("Error: Invalid choice!")
