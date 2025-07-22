import json

def init_json():
    dict = {
        "last_id": 0,
        "expenses": [

        ]
    }

    with open("budget.json", "w") as file:
        json.dump(dict, file, indent=4)
        

def main():
    init_json()

main()