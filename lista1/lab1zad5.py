print("podaj czas parkowania(w godzinach):")
czas = int(input())

if czas <= 0:
    print("bledny czas")
if czas <= 1:
    cena = 5
elif czas > 1 and czas <= 3:
    cena = 12
elif czas > 3 and czas <= 6:
    cena = 20
else:
    cena = 30

print("czas postoju: ", czas)
print("cena postoju: ", cena)