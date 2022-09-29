<<<<<<< HEAD
#Dat kost een toegangsticket per persoon van 7,45 euro voor de hele dag.
#Jullie willen ook met zijn allen voor 45 minuten in de VIP-VR-GameSeat.
#De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten.
#Jij trakteert dus betaal je alles.
antwoord = True or False
persoonen = input 
dag_kaart_per_persoon = 7.45
vijf_minuten = 0.37

persoonen = int(input("met hoe veel persoonen bent u "))
prijs1 = (dag_kaart_per_persoon * persoonen)
antwoord = input("willen jullie ook nog naar de VIP_VR_SEAT")

if antwoord == "ja":
    tijd = float(input("hoe lang willen jullie"))
    prijs2 = (vijf_minuten * tijd)
    prijs = (prijs1 + prijs2)
    print(prijs)

if antwoord == "nee":
    print(prijs1)

=======
#Dat kost een toegangsticket per persoon van 7,45 euro voor de hele dag.
#Jullie willen ook met zijn allen voor 45 minuten in de VIP-VR-GameSeat.
#De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten.
#Jij trakteert dus betaal je alles.
antwoord = True or False
persoonen = input 
dag_kaart_per_persoon = 7.45
vijf_minuten = 0.37

persoonen = int(input("met hoe veel persoonen bent u "))
prijs1 = (dag_kaart_per_persoon * persoonen)
antwoord = input("willen jullie ook nog naar de VIP_VR_SEAT")

if antwoord == "ja":
    tijd = float(input("hoe lang willen jullie"))
    prijs2 = (vijf_minuten * tijd)
    prijs = (prijs1 + prijs2)
    print(prijs)

if antwoord == "nee":
    print(prijs1)

>>>>>>> 3960045d48bd0107ca39c04eb978f49169f752b2
