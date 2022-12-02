dagen_van_de_week = ("ma", "di", "wo", "do", "vr", "za", "zo")
dag_stoppen = input("voer dag in waarop je wilt stoppen")

for dag in (dagen_van_de_week):
    print(dag)
    if dag == dag_stoppen:
        break