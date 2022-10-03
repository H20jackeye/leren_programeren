#Dat kost een toegangsticket per persoon van 7,45 euro voor de hele dag.
#Jullie willen ook met zijn allen voor 45 minuten in de VIP-VR-GameSeat.
#De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten.
#Jij trakteert dus betaal je alles.
antwoord = True or False
persoonen = input 
dag_kaart_per_persoon = 7.45
vijf_minuten = 0.37
een_minuut = (vijf_minuten / 5)
persoonen = int(input("met hoe veel persoonen bent u "))
prijs1 = (dag_kaart_per_persoon * persoonen)
antwoord = input("willen jullie ook nog naar de VIP_VR_SEAT")

if antwoord == "ja":
    tijd = float(input("hoe lang willen jullie"))
    prijs2 = (een_minuut * tijd * persoonen)
    prijs = (prijs1 + prijs2)
    print("Dit geweldige dagje-uit met" ' ',persoonen , ' ' "mensen in de speelhal met" ' ',tijd ,' ' "minuten VR kost je maar" ' ' ,prijs , ' ' "euro")

if antwoord == "nee":
    print("dit geweldige dagje-uit met" ' ',persoonen , ' ' "mensen in de speelhal kost je maar" ' ' ,prijs1 ,' ' "euro" )
#‘Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar 44.44 euro’