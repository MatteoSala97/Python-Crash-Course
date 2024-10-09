import os
print(os.getcwd())

with open(r'.\9-10-2024\24-exceptions\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    