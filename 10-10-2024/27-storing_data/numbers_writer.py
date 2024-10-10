import json
import os 

filename = r'C:\Users\matteo.sala\Documents\Python Crash Course\10-10-2024\27-storing_data\fav.json'

# Saving number 
def save_number():
    while True:
        favourite_number = input("Whats your favourite number? ")
        #checking if its a valid input
        try: 
            favourite_number = int(favourite_number)
            break
        #rasing error if triggered
        except ValueError: 
            print("That's not a valid number. Please enter a valid number.")
    #saves the number in a separate file
    with open(filename, 'w') as file_obj: 
        json.dump(favourite_number, file_obj)
    print('Number saved in a safe place.')
    
# Reads number
def get_favourite_number():
    with open(filename, 'r') as file_obj:
        saved_number = json.load(file_obj)
        print(f"I know your favourite number. It's {saved_number}!")

# Checks if the file exists: if "yes" reads it. otherwise it saves the input
if os.path.exists(filename):
    print("Your number alredy exists")
    get_favourite_number()
else:
    save_number()

