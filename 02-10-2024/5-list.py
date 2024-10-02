# Store the names of a few of your friends in a list called names . Print each person’s name by accessing each element in the list, one at a time .
names=['alex', 'mark', 'lucas', 'robert', 'jane', 'abigail']

print(names)
print(names[0]) #etc..  print(names[1])

#Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them . The text of each message should be the same, but each message should be personalized with the person’s name.
msg1="Yo!"
msg2="Hi there!"

print(msg1 + " " + names[0].title()+"!")
print(msg2 + " " + names[1].title()+"!")
print(msg1 + " " + names[2].title()+"!")

#Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples . Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle .”

motorcycles = [
    "Honda CBR500R",
    "Yamaha YZF-R3",
    "Kawasaki Ninja 400",
    "Ducati Panigale V2",
    "Harley-Davidson Iron 883"
]

for item in motorcycles:
    print("I'd like to own a " + item + ".")
    
    
#metodi per modifica aggiunta e rimozione di elementi da un array

motorcycles.append('KTM 390 Duke');
motorcycles.insert(0, 'Kawasaki Ninja ZX-10R');
motorcycles.append('Yamaha MT-09')


print(motorcycles)

del motorcycles[3];  #oppure usare il metodo .pop()
print(motorcycles)