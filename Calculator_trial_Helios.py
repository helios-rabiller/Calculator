from datetime import datetime

def calculate(a, b, op):
    """Performs basic arithmetic operations."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            print("Error: Division by zero!")
            return None
    else:
        print("Error: Operation not recognized!")
        print("Use symbols +, /, *, or - to perform a calculation.")
        return None

def add_to_history(a, b, op, result, history_file):
    """Adds a timestamped entry to the history."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(history_file, "a") as file:
        file.write(f"{now} | {a} {op} {b} = {result}\n")

def display_history(history_file):
    """Displays the calculation history."""
    try:
        with open(history_file, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No calculations recorded yet.")
                return
            print(f"{'Date and Time':<20} | {'Calculation':<20} | {'Result':<10}")
            print("-" * 50)
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("No history found.")

def clear_history(history_file):
    """Clears the content of the history file."""
    open(history_file, "w").close()
    print("History cleared.")

def replay():
    """Asks the user if they want to perform another calculation."""
    while True:
        choice = input("Do you want to perform another calculation? (yes/no) = ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("Goodbye!")
            return False
        else:
            print("Please enter only 'yes' or 'no'.")

def menu():
    """Displays the main menu and allows the user to choose an option."""
    print("\n--- Main Menu ---")
    print("1. Perform a calculation")
    print("2. Display history")
    print("3. Clear history")
    print("4. Quit")
    return input("Choose an option: ")

def calculator():
    """Main function of the calculator."""
    history_file = "data.txt"

    while True:
        choice = menu()
        if choice == "1":
            try:
                a = float(input("Value a = "))
                op = input("Operation (+, -, *, /) = ")
                if op not in ["+", "-", "*", "/"]:
                    print("Error: Operation not recognized. Please use +, -, *, or /.")
                    continue
                b = float(input("Value b = "))
                result = calculate(a, b, op)

                if result is not None:
                    print(f"Result: {result}")
                    add_to_history(a, b, op, result, history_file)
            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == "2":
            display_history(history_file)

        elif choice == "3":
            clear_history(history_file)

        elif choice == "4":
            print("Thank you for using the calculator. Goodbye!")
            break

        else:
            print("Please enter a valid number (1, 2, 3, or 4).")

# Launch the calculator
if __name__ == "__main__":
    calculator()
