import json
import os 

filename = r'C:\Users\matteo.sala\Documents\Python Crash Course\10-10-2024\27-storing_data\fav.json'


def save_number():
    favourite_number = input("Whats your favourite number? ")
    with open(filename, 'w') as file_obj: 
        json.dump(favourite_number, file_obj)
    print('Number saved in a safe place.')

def get_favourite_number():
    with open(filename, 'r') as file_obj:
        saved_number = json.load(file_obj)
        print(f"I know your favourite number. It's {saved_number}!")


if os.path.exists(filename):
    print("Your number alredy exists")
    get_favourite_number()
else:
    save_number()

