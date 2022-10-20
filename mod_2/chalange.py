#swiming garden
UITGRAVEN_m3 = 25
AFVOEREN_M3 = 32.5
VOORRIJKKOSTEN_GROOTTE = 20
VOORRIJKKOSTEN_AFSTAND = 50

meter_lang = float(input("wat is de lengte"))
meter_breed = float(input("wat is de breedte? (in m)"))
meter_diep = float(input("wat is de diepte? (in m)"))
afstand_klant = int(input("afstand in km"))

inhoud = round((meter_lang * meter_breed * meter_diep),2)
kosten_uitgraven = inhoud * UITGRAVEN_m3
kosten_afvoeren = inhoud * AFVOEREN_M3
grond_verwerken = kosten_uitgraven + kosten_afvoeren

voorrijkkosten = 0
if inhoud < VOORRIJKKOSTEN_GROOTTE and afstand_klant < VOORRIJKKOSTEN_AFSTAND:
    voorrijkkosten += 100 + 1.25 * afstand_klant
elif inhoud >= VOORRIJKKOSTEN_GROOTTE and afstand_klant >= VOORRIJKKOSTEN_AFSTAND:
    voorrijkkosten += 100 + 1.15 * afstand_klant
elif inhoud >= VOORRIJKKOSTEN_GROOTTE and afstand_klant >= VOORRIJKKOSTEN_AFSTAND:
    voorrijkkosten += 100 + 2.15 * afstand_klant
elif inhoud >= VOORRIJKKOSTEN_GROOTTE and afstand_klant >= VOORRIJKKOSTEN_AFSTAND:
    voorrijkkosten += 100 + 2.05 * afstand_klant

print(inhoud)
print(f"")



