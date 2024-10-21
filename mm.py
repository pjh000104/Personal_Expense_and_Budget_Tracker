import json

def start_software():
    create_file()
    data = get_data()

    categories = ['total_balance', 'food', 'house_hold', 'clothing', 
                  'personal_expense', 'subscription',
                  'housing_expense', 'insurance', 'other']

    print("Hello, welcome to the Personal Expense Tracker")

    for c in categories:
        while True:
            expense = input(f"Enter expense for {c}: ")
            if is_float(expense):
                data[c] = float(expense)  # Store as float
                break
            else:
                print("Error entering value. Please enter a valid number.")

    with open("info.json", "w") as file:
        json.dump(data, file)

def start_main_menu():
    print("Choose your Option: ")
    print("1: Spend money")
    print("2: Check balance")
    print("3: Reset Program")
    print("4: Quit Program")
    
    while True:
        option = input("Enter your choice: ")
        if option in ['1', '2', '3', '4']:
            break
        else:
            print("Error entering value. Please choose a valid option.")
    
    if option == '1':
        useMoney()
    elif option == '2':
        checkBalance()
    elif option == '3':
        reset()
    elif option == '4':
        print("Quitting Program. Bye bye!")
        return

def useMoney():
    data = get_data()
    while True:
        print("Type category: ")
        category = input().strip()
        
        if category not in data:
            print(f"Category '{category}' does not exist. Please try again.")
            continue  # Continue to prompt for a valid category

        break  # Exit the loop if the category is valid

    while True:
        print("Enter amount of expense: ")
        expense = input().strip()
        
        if is_float(expense):
            expense = float(expense)
            break
        else:
            print("Invalid amount entered. Please enter a valid number.")
    
    category_budget = float(data[category])

    if category_budget - expense >= 0:
        data[category] = category_budget - expense
        with open("info.json", "w") as file:
            json.dump(data, file)
        print(f"{category} has ${data[category]:.2f} left.")
    else:
        print(f"Insufficient funds in {category}. You have ${category_budget:.2f} left.")

    start_main_menu()

def checkBalance():
    data = get_data()
    total_balance = sum(float(amount) for amount in data.values())
    
    print("Balance for each category:")
    for category, amount in data.items():
        print(f"{category.capitalize()}: ${float(amount):.2f}")
    
    print(f"\nTotal Balance: ${total_balance:.2f}")
    start_main_menu()

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_string(value):
    # Check if the value is not a float and is not empty
    return not is_float(value) and value.strip() != ""

def create_file():
    with open("info.json", "w") as file:
        json.dump({
                "total_balance": 0, "food": 0, "house_hold": 0, "clothing": 0,
                "personal_expense": 0, "subscription": 0, "housing_expense": 0,
                "insurance": 0, "other": 0}, file)

def get_data():
    try:
        with open('info.json', 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        print("Data file not found or corrupted. Initializing with default values.")
        create_file()  # Create a new file with default values
        return get_data()  # Retry getting data

def reset():
    create_file()
    print("Data has been reset to default values.")
    start_main_menu()

if __name__ == "__main__":
    start_software()
    start_main_menu()