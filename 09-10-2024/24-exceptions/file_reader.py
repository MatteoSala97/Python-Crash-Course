import os
print(os.getcwd())

def dont_run():
    with open(r'.\9-10-2024\24-exceptions\pi_digits.txt') as file_object:
        contents = file_object.read()
        print(contents)


    filename = (r'.\9-10-2024\24-exceptions\pi_digits.txt')
    with open(filename) as file_object:
        for x in file_object: 
            print(x.rstrip())  #l'uso di rstrip() annienta l'utilizzo del ciclo for (che printa linea per linea)
            
filename = (r'C:\Users\matteo.sala\Documents\Python Crash Course\9-10-2024\24-exceptions\pi_million_digits.txt')

with open(filename) as file_object: 
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip() 
    
print(pi_string[:52] + "...") 
print(len(pi_string))

birthday = input("Enter your birthday, in the form ddmmyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
    
    