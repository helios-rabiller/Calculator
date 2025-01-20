import json
import os

# Path for the JSON file to store the history
HISTORY_FILE = "historique.json"

# Custom exception
class CalculatorError(Exception):
    pass

# Function to display the main menu
def display_menu():
    print("\nPython Calculator")
    print("1. Perform an operation")
    print("2. View history")
    print("3. Clear history")
    print("4. Exit")

# Function to perform a mathematical operation based on the given operator
def perform_operation(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            raise CalculatorError("Division by zero is not allowed.")
        return a / b
    elif operator == "**":
        return a ** b
    elif operator == "%":
        if b == 0:
            raise CalculatorError("Modulo by zero is not allowed.")
        return a % b
    else:
        raise CalculatorError("Invalid operator.")

# Function to prompt the user to input a number, with input validation
def prompt_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# Function to prompt the user to input a valid mathematical operator
def prompt_operator():
    while True:
        operator = input("Enter an operator (+, -, *, /, **, %): ")
        if operator in ["+", "-", "*", "/", "**", "%"]:
            return operator
        else:
            print("Invalid operator, please try again.")

# Function to load the history from a JSON file
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Error: The history file is corrupted. The history will be reset.")
                return {}
    return {}

# Function to save the history to a JSON file
def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

# Main function to manage the program
def main():
    # Load history from the JSON file
    history = load_history()
    
    # Define the next operation number
    next_operation_number = len(history) + 1
    
    while True:
        display_menu()  # Display the main menu
        choice = input("\nYour choice: ")
        
        if choice == "1":
            # Input data
            a = prompt_number("Enter the first number: ")
            operator = prompt_operator()
            b = prompt_number("Enter the second number: ")
            
            try:
                # Calculate and display the result
                result = perform_operation(a, b, operator)
                print(f"Result: {a} {operator} {b} = {result}")
                
                # Add the operation to the history
                history[str(next_operation_number)] = f"{a} {operator} {b} = {result}"
                next_operation_number += 1
                save_history(history)  # Save the history
            except CalculatorError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            # Display the history
            if history:
                print("\nOperation History:")
                for number, operation in history.items():
                    print(f"{number}: {operation}")
            else:
                print("\nNo history available.")
        
        elif choice == "3":
            # Clear the history
            history.clear()
            next_operation_number = 1  # Reset the counter
            save_history(history)  # Update the file
            print("History cleared.")
        
        elif choice == "4":
            # Exit the program
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main program
if __name__ == "__main__":
    main()
