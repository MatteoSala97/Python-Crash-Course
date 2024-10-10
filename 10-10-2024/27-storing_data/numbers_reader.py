import json

filename = r'C:\Users\matteo.sala\Documents\Python Crash Course\10-10-2024\27-storing_data\fav.json'

with open(filename) as file_obj:
    numbers = json.load(file_obj)
print(filename, 'loaded correctly.\n')
print(numbers)

