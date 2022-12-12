import random


getal1 = random.randint(1,10)
getal2 = random.randint(5,15)

number = int(input(f"En weet jij wat {getal1}+{getal2} is?"))
if number == getal1 + getal2:
    print(number)
else:
    print("wrong")