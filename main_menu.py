import json
from mm import start_main_menu


def start_software():
    create_file()
    data = get_data()
    check = 0
    count = 0
    sent = 0
    validity = 0
    sent = True
    
    categories = ['total_balance', 'food', 'house_hold', 'clothing', 
                  'personal_expense', 'subscription',
                  'housing_expense', 'insurance', 'other']
    print("Hello welcome to the Personal_Expense")
    
    data['total_balance'] = input("What is your total budget: " )
    while sent == True:    
        for c in range(1, len(categories)):
            expense = input("Enter expense for " + categories[c] + ": ")
            if is_float(expense):
                data[categories[c]] = int(expense)
                check += int(expense)
                count += 1
                print(check)
            else:
                print("Error entering value")
                break
            if check > int(data['total_balance']):
                print("Your budgeting exceeded the total budget, please re-enter all the values again")
                check = 0
                break   
            if categories[c] == 'other':
                sent = False
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
