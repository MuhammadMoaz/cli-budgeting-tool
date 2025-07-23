import json
import shlex

def init_json():
    dict = {
        "last_id": 0,
        "budget": [

        ]
    }

    with open("budget.json", "w") as file:
        json.dump(dict, file, indent=4)
        
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

def add_item(item_name):
    item_dict = {
        "id": generate_id(),
        "item_name": item_name,
        "item_type": "",
        "payment_amnt": "",
        "payment_freq": "",
        "payment_date": ""
    }

    with open("budget.json", "r+") as file:
        file_data = json.load(file)
        file_data["budget"].append(item_dict)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    
def parse_input(user_input):
    command = shlex.split(user_input)

    match command[0]:
        case "add":
            if len(command) == 2:
                add_item(command[1])
        case "update":
            print()
        case "delete":
            print()
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