

temperature = int(input(f"entrer une temperature: "))
print(f"",)

if temperature < 0:
    print("Gel")
elif temperature < 15:
    print("froid")
elif temperature < 25:
    print("doux")
else :
    print("chaud")

annee = int(input(f"entrer une annee: "))

if  annee % 4 == 0 :
    print("est bissextile")
else:
    print("non bissextile")
