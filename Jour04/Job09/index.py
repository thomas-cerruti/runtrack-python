L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

valeur = L[0]
minimum = L[0]
maximum = L[0]

for nombre in L[1:]:
    valeur += nombre
    
    if nombre < minimum:
        minimum = nombre
    
    if nombre > maximum:
        maximum = nombre

print("La valeur totale des éléments de la liste est :", valeur)
print("Le minimum dans la liste est :", minimum)
print("Le maximum dans la liste est :", maximum)