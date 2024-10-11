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
    while True: 
        try:
            with open(filename, 'r') as file_obj:
                saved_number = json.load(file_obj)
                print(f"I know your favourite number. It's {saved_number}!")
        except ValueError:
            print('The file seems to be empty or badly edited...')
            
            try:
                with open(filename, 'r') as file_obj:
                    raw_content = file_obj.read()
                    print(f"Raw content of the file: '{raw_content}'")
            except Exception as e:
                print(f"An error occurred while reading the file: {e}")
        break
    
def get_favourite_number2():
    while True:
        file_obj = open(filename, 'r')
        try:
            raw_content = file_obj.read()
            saved_number = json.load(file_obj)
            print(f"I know your favourite number. It's {saved_number}!")

        except ValueError:
            print('The file seems to be empty or badly edited...')
            print(f"Raw content of the file: '{raw_content}'")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
        file_obj.close()
        break
            

# Checks if the file exists: if "yes" reads it. otherwise it saves the input
if os.path.exists(filename):
    get_favourite_number2()
else:
    save_number()

