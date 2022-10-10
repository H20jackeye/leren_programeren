croisantjes = 17
prijscroisantjes_cent = 39
prijsproduct_croisantjes_totaal = croisantjes * prijscroisantjes_cent


stokbroden = 2
prijsstokbroden_cent = 278
prijsproduct_stokbrood_totaal = stokbroden * prijsstokbroden_cent

kortingsbonnen = 3 
kortingsprijs_cent = 50
kortingsprijs_totaal = kortingsbonnen * kortingsprijs_cent


prijs = (prijsproduct_croisantjes_totaal + prijsproduct_stokbrood_totaal - kortingsprijs_totaal ) / 100

print("de feestlunch kost",prijs ,"euro voor de" ,croisantjes , "croisantjes en de" ,stokbroden , "stokbroden als de" ,kortingsbonnen , "korting bonnen nog geldig zijn")
