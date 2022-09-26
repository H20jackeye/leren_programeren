leeftijd = 18
rijbewijs = True

if leeftijd >= 18 and rijbewijs == True:
    print("Je bent aangenomen")
else:
    print("Helaas ben je niet geschikt")

# dit is voor  als je 1 van de 2 maar nodig hebt
scooterrijbewijs = False
autorijbewijs = True

if scooterrijbewijs == True or autorijbewijs == True:
    print("Je kunt als bezorger aan de slag")
else:
    print("Je zult helaas niet snel genoeg kunnen bezorgen")