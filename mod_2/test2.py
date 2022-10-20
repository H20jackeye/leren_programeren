antwoord = " "
teller = 0

while antwoord != "stop":
    antwoord = input("voer stop in om te stoppen:")
    teller += 1
    print (teller)

print(f"aantal enter: {teller}")