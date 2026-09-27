def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def add(a, b):
    return a + b

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
            print(f"{num1} + {num2} = {add(num1, num2)}")
        else:
            print("Operation not yet fully implemented.")

if __name__ == "__main__":
    main()