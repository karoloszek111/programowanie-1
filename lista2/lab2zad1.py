zakupy = []
print("podaj liczbe produktow:")
l_produktow = int(input())

for x in range(l_produktow):
    print(f"produkt {x+1}:")
    nazwa = input()
    zakupy.append(nazwa)

print(zakupy)

print("podaj nazwe produktu do usuniecia:")
do_usuniecia = input()
if do_usuniecia in zakupy:
    zakupy.remove(do_usuniecia)
else:
    print("brak produktu na liscie")

print(zakupy)