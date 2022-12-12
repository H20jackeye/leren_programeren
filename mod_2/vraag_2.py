import random

name = input("wat is je naam")

num1 = random.randint(1,10)
num2 = random.randint(5,15)
number = int(input(f"En weet jij wat {num1}+{num2} is?"))

try:
    if number == (num1 + num2):
        print('Dat is juist')
    else:
        print('Nee dat klopt niet {}'.format(name))
except:
    print('Dat is geen nummer!')