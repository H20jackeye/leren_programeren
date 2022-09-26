getal1 = int(input("voer gatal 1 in:"))
getal2 = int(input("voer gatal 2 in:"))
actie = input("Welke actie wenst u, kies: (o)ptellen, (a)ftreken, k(volgorde), g(volgorde)")


if actie == 'a':
    zin = 'aftreken'
    antwoord = getal1 - getal2
elif actie == 'o':
    zin = 'optellen'
    antwoord = getal1 + getal2
elif actie == 'k':
    if getal1 > getal2:
        zin = "volgorde(k):" + str(getal2) + ', '+ str(getal1)
    else:
        zin = "volgorde(k):" + str(getal1) + ', '+ str(getal2)
elif actie == 'g':
    if getal1 > getal2:
        zin = "volgorde(k):" + str(getal1) + ', '+ str(getal2)
    else:
        zin = "volgorde(k):" + str(getal2) + ', '+ str(getal1)

print(antwoord)