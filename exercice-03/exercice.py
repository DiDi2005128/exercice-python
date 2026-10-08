temperatures = [12.5 , 14 , 9.5 , 17 , 21 , 19.5 , 11]

for temperature in temperatures:
   moyenne = sum(temperatures) % len(temperatures)
   minimum = min(temperatures)
   maximum = max(temperatures)

print(f"",{moyenne})
print(f"",{minimum})
print(f"",{maximum})

jours = []
for temperature in temperatures:
     if temperature > 15:
         jours.append(temperature)

print(len(jours))

f = [(temperat * 9 / 5 + 32) for temperat in temperatures]
print(f)


for i, temperature in enumerate(temperatures):
    print(f"jour {i+1} : {temperature}°c")