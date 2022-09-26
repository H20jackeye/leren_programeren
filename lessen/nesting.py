rijbewijs = input('heb je een rijbewijs?')
if rijbewijs == "ja":
    typerijbewijs = input('Heb je een auto of scooterrijbewijs')
    if typerijbewijs == "auto":
        print('je bezit een autorijbewijs')
    else:
        print('jij bezit een scooterrijbewijs')
else:
    print('helaas mag je niet rijden')