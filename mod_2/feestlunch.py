croisantjes = int(input("hoe veel croisantjes wilt u hebben ? "))
prijscroisantjes_cent = 39
prijsproduct_croisantjes_totaal = croisantjes * prijscroisantjes_cent


stokbroden = int(input("hoe veel stokbroden wil u ? "))
prijsstokbroden_cent = 278
prijsproduct_stokbrood_totaal = stokbroden * prijsstokbroden_cent

kortingsbonnen = int(input("hoe veel kortings bonen heeft u ?"))
kortingsprijs_cent = 50
kortingsprijs_totaal = kortingsbonnen * kortingsprijs_cent


prijs = (prijsproduct_croisantjes_totaal + prijsproduct_stokbrood_totaal - kortingsprijs_totaal ) / 100

print("de feestlunch kost",prijs ,"euro voor de" ,croisantjes , "croisantjes en de" ,stokbroden , "stokbroden als de" ,kortingsbonnen , "korting bonnen nog geldig zijn")
