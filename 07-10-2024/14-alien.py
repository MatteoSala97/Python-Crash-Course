# dizionari aliens
alien_0 = {
    "colore": "Verde",
    "punteggio": 10,
    "velocità": "Fast"
}

alien_1 = {
    "colore": "Giallo",
    "punteggio": 5,
    "velocità": "Mid"
}

alien_2 = {
    "colore": "Rosso",
    "punteggio": 15,
    "velocità": "Slow"
}

# printa info aliens
# for key, alien in enumerate([alien_0, alien_1, alien_2]):  
#     print(f"Alieno {key}:")
#     print(f"Colore: {alien['colore']}")
#     print(f"Punteggio: {alien['punteggio']}")
#     print(f"Velocità: {alien['velocità']}\n")
i = 1

for alien in ([alien_0, alien_1, alien_2]):  
    print(i)
    print(f"Colore: {alien['colore']}")
    print(f"Punteggio: {alien['punteggio']}")
    print(f"Velocità: {alien['velocità']}\n")
    i+=1
