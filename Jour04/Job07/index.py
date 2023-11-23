L = [8, 24, 48, 2, 16]

multiples3 = 0

for nombre in L:
    if nombre % 3 == 0:
        multiples3 += 1

print("Le nombre de multiples de 3 dans la liste est :", multiples3)