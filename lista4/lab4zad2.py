l_produktow = int(input("podaj liczbe produktow: "))
produkty = []
ceny = []
max_cena = 0
max_produkt = ""

for _ in range(l_produktow):
    nazwa_produktu = input("podaj nazwe produktu: ")
    cena_produktu = float(input("podaj cene produktu: "))
    produkty.append(nazwa_produktu)
    ceny.append(cena_produktu)

for numer, produkt in enumerate(produkty, start=1):
    print(numer, produkt)
    
for produkt, cena in zip(produkty, ceny):
    if cena>max_cena:
        max_cena = cena
        max_produkt = produkt
    print(produkt, cena)
print(list(zip(produkty, ceny)))

suma = 0
for c in ceny:
    suma += c

print("\nsuma produktow: ", suma, "\nnajdrozsza cena: ", max_cena, ":", max_produkt)
