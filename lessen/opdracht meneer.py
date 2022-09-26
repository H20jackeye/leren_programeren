naam = input('wat is uw naam?')
leeftijd = input('wat is uw leeftijd')

if leeftijd >= '18':
    print('je mag naar binnen')
else:
    print('je mag niet binnen komen')
if leeftijd <= '17':
    print('')

if naam == 'lucas' and leeftijd >= '18':
    print('je krijgt gratis drinken')