masivs = ["A", "B", "C", "D", "E", "F"]

print(masivs)
print(type(masivs))
print(masivs[3])

for x in masivs:
    print(x)

vardnica = {"Vārds":"Jānis", "Izglītība":"Vidējā","Vecums":45}

print(vardnica)
print(type(vardnica))
print(vardnica["Vārds"])

personas = [
    {"Vārds":"Jānis", "Izglītība":"Vidējā","Vecums":45},
    {"Vārds":"Viesturis", "Izglītība":"Augstākā","Vecums":27}
]

print(type(personas))

for persona in personas:
    print(persona["Vārds"])