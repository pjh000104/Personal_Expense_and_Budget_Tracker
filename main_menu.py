import json

def start_software():
    expenses = {'total': ' '}
    
    create_file()
    data = get_data()

    categories = ['total_balance', 'food', 'house_hold', 'clothing', 
                  'personal_expense', 'subscription',
                  'housing_expense', 'insurance', 'other']
    
    print("Hello welcome to the Personal_Expense")

    while True:
        print("Please enter the total expense: ")
        totalExpense = input()

        if is_float(totalExpense):
            expenses['total'] = totalExpense
            data["total_balance"] = float(totalExpense)
            break
        else:
            print("Error entering value")

    for c in categories:
        print("Enter initial expense for " + c + ": ")
        while True:
            expense = input()
            if is_float(expense):
                data[c] = float(expense)
                expenses[c] = float(expense)
                break
            else:
                print("Error entering value")

    while True:
        print("\nPlease select an option:")
        print("1. Add expense")
        print("2. Display updated balances")
        print("3. Exit")
        option = input()

        if option == "1":
            for c in categories:
                print("Enter amount spent for " + c + ": ")
                while True:
                    spent_amount = input()
                    if is_float(spent_amount):
                        result = subtract_expense(data, c, float(spent_amount))
                        if result:
                            print(f"Updated balance for {c}: {data[c]}")
                            with open("info.json", "w") as file:
                                json.dump(data, file)
                            break
                        else:
                            print("You don't have enough balance in this category.")
                            break
                    else:
                        print("Error entering value")
        elif option == "2":
            print("\nUpdated balances for each category:")
            for c in categories:
                print(f"{c}: {data[c]}")
        elif option == "3":
            break
        else:
            print("Invalid option. Please select a valid option.")

def subtract_expense(data, category, amount):
    if data[category] - amount < 0:
        return False
    else:
        data[category] -= amount
        return True

def is_float(value):
    try:
        # Try to convert the value to a float
        float(value)
        return True
    except ValueError:
        # If conversion fails, it's not a float
        return False


def create_file():
    with open("info.json", "w") as file:
        json.dump({
                "total_balance":0, "food":0, "house_hold":0, "clothing":0,
                "personal_expense":0, "subscription":0,"housing_expense":0,
                "insurance":0,"other":0}, file)
        

# A function which return's the dictionary/hashmap within the file          
def get_data():
    with open('info.json', 'r') as file:
        data = json.load(file)
        return data
start_software()