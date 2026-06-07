#storage

import json
from models import BankAccount

def load_json():
    try:
        owners = []
        with open('bank_system/accounts.json', 'r') as files:
            owners_data = json.load(files)
            for data in owners_data:
                owners.append(BankAccount(data['owner'], data['balance']))
    except (FileNotFoundError, json.JSONDecodeError):
        owners = []
    return owners 

def save_json(owners):
    owners_data = []
    for owner in owners:
        owners_data.append(owner.to_dict())
    with open('bank_system/accounts.json', 'w') as files:
        json.dump(owners_data, files, indent= 4)


