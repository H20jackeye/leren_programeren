duur = input('is de kaas belachelijk duur')
if duur == "ja":
    korst = input('zit er een korst om')
    if korst == "ja":
        print('De kaas die jij bedoelt is de emmenthaler')
    else:
         print('De kaas die jij bedoelt is de Gouda')
elif duur == "nee":
    print("de kaas die jij bedoelt is leerdammer.")
else:
    print('vul ja of nee in')