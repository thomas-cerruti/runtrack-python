nom = "ROG Strix RTX 4090 OC 24gb "
prix = 2550
stock = 3
print("nom:", nom)
print("prix:", prix)
print("stock:", stock)
quantite_achat = int(input("Veuillez mettre la quantité a acheter : "))
stock -= quantite_achat
prix += 255
print("\nAprès l'achat et l'ajustement du prix :")
print("nom:", nom)
print("prix (après inflation):", prix)
print("stock:", stock)
