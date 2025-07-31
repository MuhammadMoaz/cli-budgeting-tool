import json
import shlex
import os
from datetime import datetime

def init_json():
    dict = {
        "last_id": 0,
        "budget": [

        ]
    }

    with open("budget.json", "w") as file:
        json.dump(dict, file, indent=4)

def clear_console():
    os.system('cls')

# Add functions
def generate_id():
    # Open JSON for reading
    with open("budget.json", "r") as file:
        # Read JSON
        file_data = json.load(file)

        # Increment last_id counter
        file_data["last_id"] += 1
        id = file_data["last_id"]

        with open("budget.json", "w") as file:
            json.dump(file_data, file, indent=2)

        # Return id
        return id
    
def get_item_type():
    while True:
        item_type = input("[1] Expense or [2] Income:")
        if item_type == "1":
            item_type = "Expense"
            break
        elif item_type == "2":
            item_type = "Income"
            break
        else:
            print("Invalid input!")
    
    return item_type

def get_payment_amnt():
    while True:
        try:
            return int(input("Amount:"))
        except ValueError:
            print("NaN")
        except:
            print("Invalid Input")

def get_payment_freq():
    payment_freq_list = ["Daily", "Weekly", "Biweekly", "Monthly", "Quarterly", "Yearly"]

    while True:
        payment_freq = input("Payment Frequency:").title()
        if payment_freq in payment_freq_list:
            return payment_freq
        else:
            print("Invalid Input")

def get_payment_date():
    while True:
        payment_date = input("Payment Date (DD-MM-YYYY):")
        try:
            return str(datetime.strptime(payment_date, "%d-%m-%Y").date())
        except ValueError:
            print("Not a real date")

def get_item_details(item_name):
    return {
        "id": generate_id(),
        "item_name": item_name.title(),
        "item_type": get_item_type(),
        "payment_amnt": get_payment_amnt(),
        "payment_freq": get_payment_freq(),
        "payment_date": get_payment_date()
    }

def add_item(item_name):
    item_dict = get_item_details(item_name)

    with open("budget.json", "r+") as file:
        file_data = json.load(file)
        file_data["budget"].append(item_dict)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    
def remove_item(item_id):
    # Read JSON
    with open("budget.json", "r+") as file:
        # Load JSON data
        file_data =  json.load(file)

        # Find the task by item_id
        for item in file_data["budget"]:
            if str(item["id"]) == str(item_id):
                # Delete task
                file_data["budget"].remove(item) 
                break
       
        file.seek(0)
        file.truncate()

        # Write updated JSON back to file
        json.dump(file_data, file, indent=4)

# Update functions
def get_item_to_update(item):
    print("What would you like to update:")
    i = 1
    for key, value in list(item.items())[1:]:
        print(f"[{i}]: {key}: {value}")
        i += 1

def update_item(item_id):
    clear_console()

    # Read JSON
    with open("budget.json", "r+") as file:
        # Load JSON data
        file_data =  json.load(file)

        # Find the task by item_id
        for item in file_data["budget"]:
            if str(item["id"]) == str(item_id):
                get_item_to_update(item)
                break


def parse_input(user_input):
    command = shlex.split(user_input)

    match command[0]:
        case "add":
            if len(command) == 2:
                add_item(command[1])
        case "update":
            if len(command) == 2:
                update_item(command[1])
        case "remove":
            if len(command) == 2:
                remove_item(command[1])
        case "quit":
            print("quitting...")
            exit()
        case _:
            print("Invalid Input!")

def main():
    init_json()

    while True:
        user_input = input('budget-cli:')
        parse_input(user_input)

main()