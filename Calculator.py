
history = []

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print("Invalid operator!")
            return

        print("Result:", result)
        history.append(f"{num1} {operator} {num2} = {result}")

    except ValueError:
        print("Please enter valid numbers.")

while True:
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Calculate")
    print("2. View History")
    print("3. Clear History")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        calculator()
    elif choice == "2":
        if history:
            for item in history:
                print(item)
        else:
            print("No history available.")
    elif choice == "3":
        history.clear()
        print("History cleared!")
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
