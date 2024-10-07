dimensions=(150,40)
# print(dimensions)

#dimensions[0]= 200 #errore voluto // non si può riassegnare un valore ad una tupla così facilmente

print("original dimensions:")
for dimens in dimensions:
    print(dimens)
    
dimensions=(200, 60)
print("\nmodified dimensions: ")
for dimens in dimensions:
    print(dimens)

foods=("pizza", "pasta", "carne", "pesce", "frutta")
for food in foods:
    print("Il menù offre:",food)
    
foods=("pizza", "pasta", "carne", "verdura", "caramelle")
print("il nuovo menù offre: ")
for food in foods:
    print("- ",food)