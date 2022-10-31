from random import randint, random


aantal_complimenten = int(input("hoeveel complimenten wil je hebben"))
naam = input("wat is je naam")
vorige_random_getal = 0
#lijsten == -> variant 1 tuple random element uit de tuple
#lijsten !=  -> variant 2 4 complimenten + randint()



for x in range(aantal_complimenten):
    random_getal = randint(1, 3)
    while random_getal == vorige_random_getal:
        random_getal = randint(1, 3)

    vorige_random_getal = random_getal

    print(f"random getal = {random_getal}, vorige = {vorige_random_getal}")

    if random_getal == 1:
        print(f"je bent geweldig, {naam}")
    if random_getal == 2:
        print(f"je doet goed je best, {naam}")
    if random_getal == 3:
        print(f"je bent awsome, {naam}")
    else:
        print("")
