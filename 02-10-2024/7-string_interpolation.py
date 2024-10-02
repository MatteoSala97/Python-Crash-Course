# Presa da questo articolo    --------     https://realpython.com/python-f-strings/     ------------

#The string interpolation operator (%), or modulo operator
#The str.format() method

name= "Matteo"
last_name="Sala"
age= 27
list=['carlo', 'giacomo', 'luca']

# ---------------------------
# old style string formatting 
# ---------------------------

print("Hello, %s %s, you're %s!" % (name, last_name, age))
print("Hello, %s!" % list[0].title())

# loop per salutare tutti 
for item in list:
    print("Hello, %s!" % item.title())

# --------------------
# str.format() method 
# --------------------
 
print("Hello, I am {0} and I'm also {1} years old!" .format(name, age))

# accesso all'ordine degli argomenti in base all'index number all'interno della parentesi graffa
print("Hello, I am {1} and I'm also {0} years old!" .format(age, name)) 

# assegno un valore alle stringhe al momento del print
print("Hello, I am {name} and I'm also {age} years old!" .format(name="Luca", age="29")) 

# accedo al valore delle stringe da un array di oggetti 
user = { "name": "Antonio", "age": 33 }
print("Hello, I am {name} and I'm also {age} years old.".format(**user)) 

# altra notazione per fare la stessa cosa con f-strings
print(f"Hello, I am {user['name']} and I'm also {user['age']} years old.")

# operazioni aritmetiche
print(f"{55*3}")

#ciclo for in range
print(f"{[5**item for item in range(1, 10)]}") #[5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125]

#float limitato a 3 decimali dopo la virgola
print(format(322123.34123, ".3f"))

#formatting con f method
cool_variable="centered cool variable"
print(f"{cool_variable:=^30}")