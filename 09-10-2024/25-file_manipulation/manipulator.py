filename = (r"C:\Users\matteo.sala\Documents\Python Crash Course\9-10-2024\25-file_manipulation\file.txt")
user_list = 'USER LIST: \n'
new_users = []

while True:
    user = input("Inserisci un nome utente (o 'stop' per terminare): ")
    if user.lower() == 'stop':
        break
    new_users.append(user)
    
with open(filename, 'a+') as file_obj:
    file_obj.seek(0)
    if file_obj.readline() != user_list: 
        file_obj.write(user_list)
   
    # file_obj.seek(0, 2)
    for user in new_users:
        file_obj.write(user + '\n')
        
print("User salvato in ", filename)
