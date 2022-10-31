PRIJS_IPHONE_13 = int(input('hoe duur is de iphone'))
PRIJS_SAMSUNG_GALAXY_S22 = int(input('hoe duur is de samsung'))

verschil = (PRIJS_IPHONE_13 - PRIJS_SAMSUNG_GALAXY_S22)

if verschil > 50:
    advies = 'galaxy'
    aankoop_prijs = PRIJS_SAMSUNG_GALAXY_S22
if verschil < 50:
     advies = 'iphone'
     aankoop_prijs = PRIJS_IPHONE_13

print(f"Het advies is dus de {advies} te kopen. Het verschil is: {verschil}...")