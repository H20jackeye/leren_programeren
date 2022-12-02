grootste = 0
kleinste = 1000
aantal_deelbaar_drie = 0
for x in range(10):
    getal = int(input("voer een getal in ( boven de 0 en onder de 1000):"))
    if getal > grootste:
        grootste = getal

    if getal < kleinste:
        kleinste = getal
    
    if getal % 3 == 0:
        aantal_deelbaar_drie = aantal_deelbaar_drie + 1

print(f"Het grootste getal is: {grootste}")
print(f"Het kleinste getal is: {kleinste}")
print(f"aantal deelbaar door: {aantal_deelbaar_drie}")