bedrag = int(input("voer bedrag in :")) 

aantal_twee_euro = bedrag // 200
print(f"aantal 2 euro: {aantal_twee_euro}")
restand = bedrag - 200 * aantal_twee_euro

aantal_een_euro = bedrag // 100
print(f"aantal 1 euro: {aantal_een_euro}")
restand = restand - 100 * aantal_een_euro

aantal_50_cent = bedrag // 50
print(f"aantal 50 cent: {aantal_50_cent}")
restand = restand - 50 * aantal_50_cent

aantal_20_cent = bedrag // 20
print(f"aantal 20 cent: {aantal_20_cent}")
restand = restand - 20 * aantal_20_cent

aantal_10_cent = bedrag // 10
print(f"aantal 10 cent: {aantal_10_cent}")
restand = restand - 10 * aantal_10_cent

print(restand)
