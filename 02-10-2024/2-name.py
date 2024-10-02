# cambiare minuscole e maiuscole di una variabile salvata

name= "maTtEo sAla"
print(name.title())

print(name.upper())
print(name.lower())

#stringhe concatenate

first_name="Mario"
last_name="Rossi"
full_name=first_name+ " " + last_name

print(full_name)

# stringhe concatenate + testo 
print("Hello, " + full_name.title() + " and welcome to the python crash course!" )

#salvato in varabile
greet= ("Hello, " + full_name.title() + " and welcome to the python crash course!" )
print(greet)

# aggiungere a capo ad un comando 
print("Hello \nWorld \nBut \nWith \nWhitespaces")