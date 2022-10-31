#De functionaliteiten die in de applicatie moeten zitten zijn:
#de klant kan een keuze maken uit 3 afmetingen pizza's, namelijk: small, medium en large. Voor elke afmeting wordt er gevraagd hoeveel pizza's de klant wil.
#Toon op het scherm met goede omschrijving het aantal bestelde pizza's voor elke afmeting en berekenen per afmeting de prijs uit
#Toon op het scherm de totaalprijs van alle pizza's.
#Bovenaan in de Python file noteer je als commenteer het volgende: voornaam, achternaam en opdracht: Pizza calculator
#De volgende zaken dienen ook op orde te zijn:

#leesbare layout van de code
#naamgeving is duidelijk en 'self explaining'
#er is passend commentaar toegevoegd in de code
#laat de uitkomst er uit zien als een bonnetje

#Test het programma grondig. Maak daarvan printscreens .

#Commmit en push pizzaCalculator.py

#Lever hier het programma + screenshot in.

 #Lucas van eijnsbergen Opdracht: pizza calculator

MARGHERITA = 3.00  
HAWAII = 3.14
SALAMI = 3.79

vraag = input("hallo, goede dag wat wilt u bestelen: ")

if vraag == "margherita":
    pizza_prijs = MARGHERITA

elif vraag == "hawaii":
    pizza_prijs = HAWAII

elif vraag == "salami":
    pizza_prijs = SALAMI

if vraag == "margherita":
    pizza_soort = "pizza-margherita"

elif vraag == "hawaii":
   pizza_soort = "pizza-hawaii"

elif vraag == "salami":
   pizza_soort = "pizza-salami"

pizza_aantal = int(input("hoe veel pizza`s wilt u?"))
    
pizza_grootte = input("hoe groot wilt u de pizza, 'small', 'medium', 'large'?.")

large = 0.25

meduim = pizza_prijs

small = 0.25

if pizza_grootte == 'large':
    zin = 'large optellen'
    antwoord = (pizza_prijs + large) * pizza_aantal

if pizza_grootte == 'medium':
 zin = 'medium'
 antwoord = pizza_prijs * pizza_aantal

if pizza_grootte == 'small':
    zin = 'small aftrekken'
    antwoord = (pizza_prijs - small) * pizza_aantal

print("--------------------------------------------")
print(f"| pizza: {pizza_soort}                     ")
print(f"| *                                        ")
print(f"| hoeveel heid: {pizza_aantal}             ")
print(f"| *                                        ")
print(f"| *                                        ")
print(f"| pizza groote: {pizza_grootte}            ")
print(f"| *                                        ")
print(f"| *                                        ")
print(f"| *                                        ")
print(f"| *                                        ")
print(f"| *                                        ")
print(f"| * totaal:[{antwoord}]                    ")
print(f"| *                                        ")
print("--------------------------------------------")








