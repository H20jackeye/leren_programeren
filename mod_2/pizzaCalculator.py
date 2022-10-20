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

margherita = float(3.00)  
hawaii = float(3.14)
salami = float(3.79)

pizza_soort = input("hallo, goede dag wat wilt u bestelen: ")

if pizza_soort == "margherita":
    pizza_soort = margherita

elif pizza_soort == "hawaii":
    pizza_soort = hawaii

elif pizza_soort == "salami":
    pizza_soort = salami

pizza_aantal = int(input("hoe veel pizza`s wilt u?"))
    
pizza_grootte = input("hoe groot wilt u de pizza, 'small', 'medium', 'large'?.")

large = float(0.25)

meduim = pizza_soort

small = float(0.25)

if pizza_grootte == 'large':
    zin = 'large optellen'
    antwoord = (pizza_soort + large) * pizza_aantal

if pizza_grootte == 'medium':
 zin = 'medium'
 antwoord = (pizza_soort) * pizza_aantal

if pizza_grootte == 'small':
    zin = 'small aftrekken'
    antwoord = (pizza_soort - small) * pizza_aantal

print("--------------------------------------------")
print(f"| pizza: {antwoord}                        ")
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








