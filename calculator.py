def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

def main():
    while True:
        print("\n--- Calculator Master ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Select an operation (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please select from 1-5.")
            continue
            
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        print("\n--- Result ---")
        if choice == '1':
            print(f"When you add {num1} and {num2} together, the total sum is {add(num1, num2)}.")
        elif choice == '2':
            print(f"If you subtract {num2} from {num1}, the remaining difference is {subtract(num1, num2)}.")
        elif choice == '3':
            print(f"Multiplying {num1} by {num2} gives you a final product of {multiply(num1, num2)}.")
        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(f"Calculation failed: {result}") 
            else:
                print(f"Dividing {num1} by {num2} results in {result}.")

if __name__ == "__main__":
    main()


    # End of calculator code