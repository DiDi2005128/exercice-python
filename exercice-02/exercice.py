

#temperature = int(input(f"entrer une temperature: "))

#if temperature < 0:
#    print("Gel")
#elif temperature < 15:
 #   print("Froid")
#elif temperature < 25:
 #   print("Doux")
#else :
 #   print("Chaud")

annee = int(input(f"Entrer une annee: "))

if  annee % 4 == 0 and annee % 100 or 400 != 0 :
    print("est bissextile")
else:
    print("non bissextile")
