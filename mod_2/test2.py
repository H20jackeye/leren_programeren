enc = "PXDMn!?BdNhP!?e"
next = False
uitroep_gevonden = False
vraagteken_gevonden = False
decrypted_zin = ""

for c in enc:
    print(c)
    print(next)
    print(uitroep_gevonden)
    print(vraagteken_gevonden)

    if next:
         decrypted_zin += c
         next = False

vraagteken_gevonden = c == "?"
next = vraagteken_gevonden and uitroep_gevonden
uitroep_gevonden = c == "!"

print(next)

print(decrypted_zin)
