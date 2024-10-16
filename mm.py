import json


def start_main_menu():
    print("Choose your Option: ")
    print("1: Spend money")
    print("2: Check balance")
    print("3: Reset Program")
    print("4: Quit Program")
    while True:
        option = input()
        if is_float(option):
            break
        else:
            print("Error entering value")
    if option == '1':
        useMoney()
    # elif option == 2:
    #     checkBalance()
    elif option == '3':
        reset()
    elif option == '4':
        print("quitting Program byebye")
        return


def useMoney():
    data = get_data()
    print("type category: ")
    category = input()
    print("Enter amount of expense: ")
    expense = float(input())
    category_budget = float(data[category])

    if category_budget-expense >= 0:
        data[category] = category_budget - expense

    with open("info.json", "w") as file:
        json.dump(data, file)

    print(category, "has $", data[category], "left.")
    start_main_menu()


def is_float(value):
    try:
        # Try to convert the value to a float
        float(value)
        return True
    except ValueError:
        # If conversion fails, it's not a float
        return False
    

def get_data():
    with open('info.json', 'r') as file:
        data = json.load(file)
        return data


def reset():
    from main_menu import start_software
    start_software()
