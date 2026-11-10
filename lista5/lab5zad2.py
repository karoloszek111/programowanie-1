import numpy as np

l_produktow = int(input("podaj liczbe produktow: "))

produkty = np.array([])

for x in range(l_produktow):
    produkt = int(input(f"podaj cene {x+1}:"))
    produkty = np.append(produkty, produkt)

rabat = int(input("podaj rabat (%): "))

po_rabacie = produkty * (1.0 - rabat / 100.0)

print(f"suma produktow: {np.sum(produkty)}")
print(f"suma produktow po rabacie: {np.sum(po_rabacie)}")
powyzej_100 = po_rabacie[po_rabacie > 100.0]
print(f"ceny po rabacie powyzej 100zl: {powyzej_100}")