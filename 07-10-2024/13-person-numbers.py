# 6-1. Person: Use a dictionary to store information about a person you know . 
# Store their first name, last name, age, and the city in which they live . You should have keys such as first_name, last_name, age, and city . Print each piece of information stored in your dictionary .

person = {
    'first_name': 'Mario',
    'last_name': 'Rossi',
    'age': 30,
    'city': 'Roma'
}

for item, value in person.items():
    print(f"{item}: {value}")
    
# Creazione del dizionario per i numeri preferiti
favorite_numbers = {
    'Giovanni': 4,
    'Maria': 12,
    'Luca': 42,
    'Francesca': 22,
    'Alessandro': 111
}

for key, value in favorite_numbers.items():
    print(f"{key}: {value}\n")
    
# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers . 
# Think of five names, and use them as keys in your dictionary . Think of a favorite number for each person, and store each as a value in your dictionary . Print each person’s name and their favorite number . For even more fun, poll a few friends and get some actual data for your program .
    
glossary = {
    'Variabile': 'Un contenitore per memorizzare dati.',
    'Funzione': 'Un blocco di codice che esegue un compito specifico.',
    'Dizionario': 'Una raccolta di coppie chiave-valore.',
    'Lista': 'Una raccolta ordinata di elementi.',
    'Ciclo': 'Un costrutto che ripete un blocco di codice.'
}

for word in glossary.keys(): 
    print(f"{word}: {glossary[word]}\n")
    
    
# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through . One key-value pair might be 'nile': 'egypt' .
# • Use a loop to print a sentence about each river, such as The Nile runs through Egypt .
# • Use a loop to print the name of each river included in the dictionary .
# • Use a loop to print the name of each country included in the dictionary .
       
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

# Stampa frase fiume
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print()
# Stampa fiume
print("Rivers included in the dictionary:")
for river in rivers.keys():
    print(river)

print()

# Stampa paese
print("Countries included in the dictionary:")
for country in rivers.values():
    print(country)
