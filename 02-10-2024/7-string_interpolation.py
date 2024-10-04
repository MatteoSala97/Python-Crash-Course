# Presa da questo articolo    --------     https://realpython.com/python-f-strings/     ------------

#The string interpolation operator (%), or modulo operator
#The str.format() method
from datetime import datetime



name= "Matteo"
last_name="Sala"
age= 27
list=['carlo', 'giacomo', 'luca']

dizionario= {
    'name': 'antonio',
    'cognome': 'rossi'
}

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

# accedo al valore delle stringhe da un dizionario
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


# ----------------------
# f notation excercises
# ----------------------

# -1
f_name="Luca"
f_age= 33

f_greet= print(f"Ciao mi chiamo {f_name} e ho {f_age} anni.")

# -2 
base=5
length=10
area= base * length

print(f"L'area calcolata è di {area} cm.") 
#// oppure
print(f"L'area calcolata è di {base*length} cm.")

# -3
price = 100
iva = 0.21 
total_price= price * (1+ iva)

print(f"Il prezzo ivato è {total_price:.2f} €")

#-4 
today= datetime.now()
# print(f"Today is {today}")
formatted_date= today.strftime("%d/%m/%Y")
formatted_time= f"{today.hour}:{today.minute}:{today.second}"

print(f"Oggi è il {formatted_date} e sono le {formatted_time}")
