print("podaj temperature(w stopniach celsjusza): ")
temp = float(input())
ogrzewanie = "wylaczone"
powod = "bez zmian"
print("czy ktos jest w domu(tak/nie)? ")
if input() == "tak":
    domownik = True
else:
    domownik = False

print("czy okno jest otwarte(tak/nie)? ")
if input() == "tak":
    okno_otw = True
else:
    okno_otw = False

if okno_otw:
    ogrzewanie = "wylaczone"
    powod = "okno otwarte"
else:
    if domownik and temp <= 20:
        ogrzewanie = "wlaczone"
        powod = "domownik w domu, temperatura ponizej 20 stopni"
    elif domownik == False and temp <= 16:
        ogrzewanie = "wlaczone"
        powod = "pusty dom okna zamkniete, temperatura ponizej 16 stopni"
print(ogrzewanie, powod)