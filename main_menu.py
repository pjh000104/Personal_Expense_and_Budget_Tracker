def start_software():
    expenses = {'total': ' '                 
                }
    categories = ['cat1', 'cat2']
    print("Hello welcome to the Personal_Expense")

    while True:
        print("Please enter the total expense: ")
        totalExpense = input()
        if is_float(totalExpense):
            expenses[totalExpense] = totalExpense
            break
        else:
            print("Error entering value")

    for c in categories:
        while True:
            expense = input()
            if is_float(totalExpense):
                expenses[c] = expense
                break
            else:
                print("Error entering value")


def is_float(value):
    try:
        # Try to convert the value to a float
        float(value)
        return True
    except ValueError:
        # If conversion fails, it's not a float
        return False


start_software()