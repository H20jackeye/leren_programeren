#Maak een programma person.py dat de gebruiker om zijn naam, adres, postcode en woonplaats vraagt met duidelijke prompts.
#Laat het programma daarna een adreskaart (met lijntjes) tonen in de terminal:

print("-----------------------------------------------------------------")
print("dit is een vragen lijst vul deze alstublieft even in")
naam = input("wat is uw naam")
achternaam = input ("wat is uw achternaam")
postcode = input ("wat is uw postcode")
woonplaats = input("hoe heet uw woon plaats")
geboorte_datum = input("wanneer bent u gebooren")
print("bedankt voor het invulen")
print("-----------------------------------------------------------------")




print(" ----------------------------------------------------------------")
print(f"|Naam = {naam}                                                  ")
print(f"|Achternaam = {achternaam}                                      ")
print(f"|Postcode = {postcode}                                          ")
print(f"|Woonplaats = {woonplaats}                                      ")
print(f"|Geborte datum = {geboorte_datum}                               ")
print(" ----------------------------------------------------------------")