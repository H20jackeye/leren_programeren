land_1_naam = input("welk land is land nummer 1 in Groep A: ")
land_2_naam = input("welk land is land nummer 2 in Groep A: ")
land_3_naam = input("welk land is land nummer 3 in Groep A: ")

#wedstrijd_1 = land_1 + land_2
#wedstrijd_2 = land_2 + land_3
#wedstrijd_3 = land_1 + land_3

w_1_sc_land_1 = input(f"wat is de scoren van: {land_1_naam}")
wedstrijd_1_scoren_land_2 = input(f"wat is de scoren van: {land_2_naam}")

if w_1_sc_land_1 > wedstrijd_1_scoren_land_2:
    winaar_w_1 = w_1_sc_land_1
if wedstrijd_1_scoren_land_2 > w_1_sc_land_1:
    winaar_w_1 = wedstrijd_1_scoren_land_2

doelsaldo_winaar_1 = + 3
doelsaldo_loser_1 = - 3

land_1_totaal_punten_scoren = 0
land_2_totaal_punten_scoren = 0
land_3_totaal_punten_scoren = 0

if winaar_w_1 == w_1_sc_land_1:
    doelsaldo_winaar_1 = land_1_totaal_punten_scoren

if doelsaldo_winaar_1 == land_1_totaal_punten_scoren:
    doelsaldo_loser_1 = land_2_totaal_punten_scoren

if winaar_w_1 == wedstrijd_1_scoren_land_2:
    doelsaldo_winaar_1 = land_2_totaal_punten_scoren

if doelsaldo_winaar_1 == land_2_totaal_punten_scoren:
    doelsaldo_loser_1 = land_1_totaal_punten_scoren

print(land_1_totaal_punten_scoren)
print(land_2_totaal_punten_scoren)
print(land_3_totaal_punten_scoren)
print(doelsaldo_winaar_1)
print(doelsaldo_loser_1)
