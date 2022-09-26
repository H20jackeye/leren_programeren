fysiek = input("is het spel fysiek")
if fysiek == "ja":
    bordspel = input("is het een bord spel")
    if bordspel == "nee":
        oranje = input("is het spel oranje")
        if oranje == "ja":
            print("het is het kaartspel")
        elif oranje == "nee":
            print("het is sushi go")
    elif bordspel == "ja":
        treintjes = input("heeft het spel treintjes")
        if treintjes == "ja":
            print("Ticket to ride")
        elif treintjes == "nee":
            print("Catan")
elif fysiek == "ja":
    sport = input("is het een sportspel")
    if sport == "ja":
        print("Fifa 23")
    elif sport == "nee":
        print("AOE 4")