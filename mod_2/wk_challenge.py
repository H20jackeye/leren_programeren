land_1_naam = input("welk land is land nummer 1 in Groep A: ")
land_2_naam = input("welk land is land nummer 2 in Groep A: ")
land_3_naam = input("welk land is land nummer 3 in Groep A: ")

#wedstrijd_1 = land_1 + land_2
#wedstrijd_2 = land_2 + land_3
#wedstrijd_3 = land_1 + land_3

wedstrijd_1_scoren_land_1 = 0 
wedstrijd_1_scoren_land_2 = 0
wedstrijd_1_scoren_land_3 = 0 

wedstrijd_1_scoren_land_1 = input(f"wat is de scoren van: {land_1_naam}")
wedstrijd_1_scoren_land_2 = input(f"wat is de scoren van: {land_2_naam}")

if wedstrijd_1_scoren_land_1 > wedstrijd_1_scoren_land_2:
    winaar_wedstrijd_1 = wedstrijd_1_scoren_land_1
if wedstrijd_1_scoren_land_2 > wedstrijd_1_scoren_land_1:
    winaar_wedstrijd_1 = wedstrijd_1_scoren_land_2

doelsaldo_winaar_1 = + 3
doelsaldo_loser_1 = - 3

land_1_doelsaldo_punten = 0
land_2_totaal_punten_scoren = 0
land_3_totaal_punten_scoren = 0

if winaar_wedstrijd_1 == wedstrijd_1_scoren_land_1:
    land_1_doelsaldo_punten = doelsaldo_winaar_1

if doelsaldo_winaar_1 == land_1_doelsaldo_punten:
    land_2_totaal_punten_scoren = doelsaldo_loser_1

if winaar_wedstrijd_1 == wedstrijd_1_scoren_land_2:
    land_2_totaal_punten_scoren = doelsaldo_winaar_1

if doelsaldo_winaar_1 == land_2_totaal_punten_scoren:
    land_1_doelsaldo_punten = doelsaldo_loser_1
print("-------------------------------------------------------------------")
print(f"wedstrijd {land_1_naam} - {land_2_naam} eindigde in: {wedstrijd_1_scoren_land_1} - {wedstrijd_1_scoren_land_2}")
print("Overzicht Groep A")
print(f"{land_1_naam}: punten: {wedstrijd_1_scoren_land_1} doelsaldo: {land_1_doelsaldo_punten}")
print(f"{land_2_naam}: punten: {wedstrijd_1_scoren_land_2} doelsaldo: {land_2_totaal_punten_scoren}")
print(f"{land_3_naam}: punten: {wedstrijd_1_scoren_land_3} doelsaldo: {land_3_totaal_punten_scoren}")
print("-------------------------------------------------------------------")

#WEDSTRIJD 2

wedstrijd_2_scoren_land_1 = 0 
wedstrijd_2_scoren_land_2 = 0
wedstrijd_2_scoren_land_3 = 0 

wedstrijd_2_scoren_land_2 = input(f"wat is de scoren van: {land_2_naam}:")
wedstrijd_2_scoren_land_3 = input(f"wat is de scoren van: {land_3_naam}:")

if wedstrijd_2_scoren_land_2 > wedstrijd_2_scoren_land_3:
    winaar_wedstrijd_2 = wedstrijd_1_scoren_land_2
if wedstrijd_2_scoren_land_3 > wedstrijd_1_scoren_land_2:
    winaar_wedstrijd_2 = wedstrijd_1_scoren_land_3

land_1_doelsaldo_punten_w2 = 0
land_2_doelsaldo_punten_w2 = 0
land_3_doelsaldo_punten_w2 = 0

if winaar_wedstrijd_2 == wedstrijd_2_scoren_land_2:
    land_2_doelsaldo_punten_w2 = doelsaldo_winaar_1

if doelsaldo_winaar_1 == land_2_doelsaldo_punten_w2:
    land_3_doelsaldo_punten_w2 = doelsaldo_loser_1

if winaar_wedstrijd_2 == wedstrijd_2_scoren_land_3:
    land_3_doelsaldo_punten_w2 = doelsaldo_winaar_1

if doelsaldo_winaar_1 == land_3_doelsaldo_punten_w2:
    land_2_doelsaldo_punten_w2 = doelsaldo_loser_1

print("-------------------------------------------------------------------")
print(f"wedstrijd {land_2_naam} - {land_3_naam} eindigde in: {wedstrijd_2_scoren_land_2} - {wedstrijd_2_scoren_land_3}")
print("Overzicht Groep A")
print(f"{land_1_naam}: punten: {wedstrijd_2_scoren_land_1} doelsaldo: {land_1_doelsaldo_punten_w2}")
print(f"{land_2_naam}: punten: {wedstrijd_2_scoren_land_2} doelsaldo: {land_2_doelsaldo_punten_w2}")
print(f"{land_3_naam}: punten: {wedstrijd_2_scoren_land_3} doelsaldo: {land_3_doelsaldo_punten_w2}")
print("-------------------------------------------------------------------")

#WEDSTRIJD 3