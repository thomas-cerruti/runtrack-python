n=int(input("saisissez une table:"))
for nb in range(1,n+1):
    print("voici la table de multi de ",nb)
    for i in range(1,11):
        print(i, "x", nb , " = ", i*nb)