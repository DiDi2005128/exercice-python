ventes = [
    {"produit": "café", "prix": 2.5, "quantite": 120},
    {"produit": "thé", "prix": 2.0, "quantite": 80},
    {"produit": "jus", "prix": 3.5, "quantite": 45},
]

ca_par_produit = {vente["produit"] : vente["prix"] * vente["quantite"] for vente in ventes}
print("chiffre d'affaire par produit: ", ca_par_produit)

ca_total = sum(ca_par_produit.values())
print(f"ca_total = ", ca_total)

maximum = max(ca_par_produit, key= ca_par_produit.get)
print(maximum)