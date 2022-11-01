#Equal to ==
#Not equal to !=
#Greater than >
#Less than <
#Greater than or equal to >=
#Less than or equal to <=
start = input("is de kaas geel?")
if start == 'ja':
    gaten = input("zitten er gaten in de kaas?")
    if gaten == 'ja':
        prijs = input("is de kaas belachelijk duur?")
        if prijs == 'ja':
            print("jou kaas heet emmenthaler")
        if prijs == 'nee':
            print("jou kaas heet leerdammer")
    if gaten == 'nee':
        hard = input("is de kaas hard als steen?")
        if hard == 'ja':
            print("jou kaas heet parmigiano reggiano")
        if hard == 'nee':
            print("jij hebt goudse kaas")
if start == 'nee':
    schimmel = input("heeft de kaas blauwe schimmel?")
    if schimmel == 'ja':
        korst = input("heeft de kaas een korst?")
        if korst == 'ja':
            print("de naam van jou kaas is blue de rochbaron")
        if korst == 'nee':
            print("jou kaas heet foume d'ambert")
    if schimmel == 'nee':
        korst = input("heeft de kaas een korst?")
        if korst == 'ja':
            print("jou kaas heet camembert")
        if korst == 'nee':
            print(" de naam van jou kaas is mozzarella")