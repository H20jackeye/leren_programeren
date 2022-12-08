print("|-------------------------------------------------------|")
print("|              Sollicitatie Formulier                   |")
print("|                                                       |")
print("|-------------------------------------------------------|")
print("|Er worden een paar relevanten vragen aan je gesteld ...|")
print("|Voer A.U.B in wat u allemaal all weet                  |")
print("|Als u voldoet aan alle benodigd heden dan komt er een  |")
print("|Sollicitatie gesprek!!                                 |")
print("|Dus blijf rustig en blijf gefocused                    |")
print("|-------------------------------------------------------|")
naam = input("|wat is uw naam ?: ")
leeftijd = int(input("|hoe oud ben je?: "))
if leeftijd >= 18:
    leeftijd_voldoet = True
else:
    leeftijd_voldoet = False

Diploma_mbo_4 = input("|ben je in bezit van een Mbo 4 Diploma? J/N : ")
if Diploma_mbo_4 == "j":
    heeft_diploma_mbo4 = True
else:
    heeft_diploma_mbo4 = False

geldig_vrachtwagen_rijbewijs = input("|bent u in bezit van een geldig vrachtwagen rijbewijs j/n? : ")
if geldig_vrachtwagen_rijbewijs == "j":
    heeft_geldig_vrachtwagen_rijbewijs = True
else:
    heeft_geldig_vrachtwagen_rijbewijs = False


hoge_hoed = input("|bent u in bezit van een hoge hoed j/n? : ")
if hoge_hoed == "j":
    heeft_hoge_hoed = True
else:
    heeft_hoge_hoed = False



man_of_vrouw = input("|wat is uw geslacht m/v? : ")
if man_of_vrouw == "m":
    #'Man'
    snor = input("|heeft u een snor van minimaal 10cm breed j/n? :")
    if snor == "j":
        heeft_snor = True
    else:
        heeft_snor = False



if man_of_vrouw == "v":
    #'Vrouw'
    haar_kleur = input("|heeft u rood haar? j/n? :")
    if haar_kleur == "j":
        heeft_rood_haar = True
    else:
        heeft_rood_haar = False

    if haar_kleur == "j" or "n":
        haar_lengte = int(input("|hoe lang is je haar? : ")) 
        if haar_lengte >= 20:
            heeft_juiste_haar_lengte = True
        else:
            heeft_juiste_haar_lengte = False

lengte_persoon = int(input("|hoe lang ben je?"))
if lengte_persoon >= 150 and lengte_persoon <= 220:
    is_lang_genoeg = True
else:    
    is_lang_genoeg = False

#Is zwaarder dan 90 kg en lichter dan 120 kg

gewicht = int(input("|hoeveel weeg je?"))
if gewicht >= 90 and gewicht <= 120:
    weegt_genoeg = True
else:
    weegt_genoeg = False
    
#Heeft Certificaat “Overleven met gevaarlijk personeel”
certificaat = input("|heb je een certificaat voor “Overleven met gevaarlijk personeel”? J/N ")
if certificaat == "j":
    heeft_certificaat = True
else:
    heeft_certificaat = False

# Meer dan 4 jaar praktijkervaring met dieren-dressuur OF
# meer dan 5 jaar ervaring met jongleren OF meer dan 
# 3 jaar praktijkervaring met acrobatiek.
# Let op: Vraag de jaren ervaring afzonderlijk voor alle kunsten: dieren-dressuur, jongleren én acrobatiek. Dus 3 vragen!
praktijk_ervaring = input("|heb je praktijk ervaring met een van deze praktijken?. dierendressuur, jongleren, acrobatiek (j/n)")
if praktijk_ervaring == "j":
    heeft_praktijk_ervaring = True
else:
    heeft_praktijk_ervaring = False

if praktijk_ervaring == "j":
    praktijken = input("|welke praktijk deed je?: dierendressuur, jongleren, acrobatiek,")
    if praktijken == "dierendressuur":
        DIERENDRESSUUR = "dierendressuur"
    if praktijken == "jongleren":
        JONGLEREN = "jongleren"
    if praktijken == "acrobatiek":
        ACROBAATIEK = "acrobatiek"
if praktijk_ervaring == "j":
    jaar_ervaring = int(input("|hoe veel jaar deed je het?"))

if praktijk_ervaring == "j":
    if praktijken == "dierendressuur" and jaar_ervaring >= 4:
        dierendressuur = True
    else:
        dierendressuur = False

    if praktijken == "jongleren" and jaar_ervaring >= 5:
        jongleren = True
    else:
        jongleren = False

    if praktijken == "acrobatiek" and jaar_ervaring >= 3:
        acrobatiek = True
    else:
        acrobatiek = False


print("|-------------------------------------------------------")
print("|-------------ANTWORDEN OP DE VRAGEN--------------------")
print("|-------------------------------------------------------")

print(f"|leeftijd = {leeftijd_voldoet}")
print(f"|diploma = {heeft_diploma_mbo4}")
print(f"|vrachtwagen rijbewijs = {heeft_geldig_vrachtwagen_rijbewijs}")
print(f"|bezit van een hoge hoed = {heeft_hoge_hoed}")
print(f"|het geslacht is een = {man_of_vrouw}")
if man_of_vrouw == "m":
    print(f"|heeft een snor van minimaal 10 cm = {heeft_snor}")

if man_of_vrouw == "v":
    print(f"|vraag of je rood haar had was = {heeft_rood_haar}")
    if man_of_vrouw == "v":
        print(f"|je haar was minimaal 20cm lang = {heeft_juiste_haar_lengte}")
        if man_of_vrouw == "v":
            print(f"|haar lengte is = {haar_lengte}")
print(f"|je bent lang genoeg = {is_lang_genoeg}")
print(f"|je weegt meer dan 90 kg en lichter dan 120 kg  = {weegt_genoeg}")
print(f"|je hebt het certificaat = {heeft_certificaat}")

if praktijk_ervaring == "j":
    print(f"|heb je practijk ervaring = {heeft_praktijk_ervaring}")
    print(f"|welke praktijk deed je = {praktijken}")
    print(f"|hoeveel jaar doe je dit all {jaar_ervaring}")

else:
    print(f"|heb je practijk ervaring = {heeft_praktijk_ervaring}")

print("|-------------------------------------------------------")
if man_of_vrouw == "m":
    if leeftijd_voldoet and heeft_diploma_mbo4 and heeft_geldig_vrachtwagen_rijbewijs and heeft_hoge_hoed and heeft_snor and is_lang_genoeg and weegt_genoeg and heeft_certificaat and dierendressuur or jongleren or acrobatiek == True:
        print("|-------------------------------------------------------")
        print("|---je bent geschikt voor het werk we zien je maandag---")
        print("|-------------------------------------------------------")
    else:
        print("|-------------------------------------------------------")
        print("|---------je bent niet geschikt voor het werk-----------")
        print("|-------------------------------------------------------") 



if man_of_vrouw == "v":
    if leeftijd_voldoet and heeft_diploma_mbo4 and heeft_geldig_vrachtwagen_rijbewijs and heeft_hoge_hoed and heeft_rood_haar and heeft_juiste_haar_lengte and is_lang_genoeg and weegt_genoeg and heeft_certificaat and dierendressuur or jongleren or acrobatiek == True:
        print("|-------------------------------------------------------")
        print("|---je bent geschikt voor het werk we zien je maandag---")
        print("|-------------------------------------------------------")
    else:
        print("|-------------------------------------------------------")
        print("|---------je bent niet geschikt voor het werk-----------")
        print("|-------------------------------------------------------")
    
print("lol")