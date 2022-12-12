#programma wa om namen vraagt, om leeftijden vraagt,
#dit opslaat in een dicht en vervolgens de hoogste leeftijd print.
# data opslag (keys en values)
mijn_namen_dict = {}
#loop en een half
while True:
    naam = input("wat is je naam? (stop om te stoppen) ")
    if naam == "stop":
        break
   
    if naam in mijn_namen_dict:
        if input("wilt u bijwerken? ja/nee") != "ja":
            continue
        else:
            break
        
    #toevoegen of bijwerken van dictionary
    leeftijd = int(input("wat is je leeftijd? "))
    if leeftijd in mijn_namen_dict.values():
        for n, j in mijn_namen_dict.items():
            if j == leeftijd:
                break
        print(f"{n} is al zo OUD!!!")
        if input("toch doorgaan? (ja/nee)") != "ja":
            continue
    

mijn_namen_dict.update({naam : leeftijd})

print(mijn_namen_dict)    

leeftijd_lijst = list(mijn_namen_dict.values())
namen_lijst = list(mijn_namen_dict.keys())
print(leeftijd_lijst)
print(max(leeftijd_lijst))
print(namen_lijst[namen_lijst.index(max(leeftijd_lijst))])