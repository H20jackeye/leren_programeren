



CONSOLE_PRIJS = 55
PC_PRIJS = 45
MEMBER_KORTING = 15
platform = input('ben je pc of console gamer?')
prijs = CONSOLE_PRIJS# dit is de prijs van een consolegame

if platform == 'pc':
    prijs = PC_PRIJS

if platform == 'console':
    prijs = CONSOLE_PRIJS

if platform == 'member kortning':
    prijs = MEMBER_KORTING

print (f'U bent {platform} gamer, dan kost de game: {prijs} Euro')
