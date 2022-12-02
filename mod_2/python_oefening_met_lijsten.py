
from random import choice

mylist = [5, 12, 19, 27, 3,]
print(mylist)
mylist.append(25)
print(mylist)

print(len(mylist))

mylist.append(12)
print(mylist)
mylist.remove(12)
print(mylist)


naam_lijst = []
naam = input("voer een naam in, of quit")
while naam != "quit":
    naam_lijst.append(naam)
    naam = input("voer een naam in, of quit")

print(naam_lijst)
print(choice(naam_lijst))

mylist.pop(0)
print(mylist)


mylist.insert(0, 36)
print(mylist)

mylist2 = [1, "aap", 2, "apen", 3, "watermeloen", 15, 27]
for e in mylist2:
    typ = str(type(e))
    if typ == "<class 'int'>":
        teller += 1
print(teller)