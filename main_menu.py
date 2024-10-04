import json
from mm import start_main_menu


def start_software():
    expenses = {'total': ' '
                }
    
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
            expenses[totalExpense] = totalExpense
            data["total_balance"] = totalExpense
            break
        else:
            print("Error entering value")

    for c in categories:
        print("Enter expense for " + c + ": ")
        while True:
            expense = input()
            if is_float(totalExpense):
                data[c] = expense
                expenses[c] = expense
                break
            else:
                print("Error entering value")
    with open("info.json", "w") as file:
        json.dump(data, file)


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
start_main_menu()
