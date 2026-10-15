print("podaj liczbe punktow: ")
liczba_pkt = float(input())
if liczba_pkt < 0 or liczba_pkt > 100:
    print("blad")
    liczba_pkt = float(input())

if liczba_pkt >= 0 and liczba_pkt <= 49:
    ocena = 2
elif liczba_pkt >= 50 and liczba_pkt <= 59:
    ocena = 3
elif liczba_pkt >= 60 and liczba_pkt <= 69:
    ocena = 3.5
elif liczba_pkt >= 70 and liczba_pkt <= 79:
    ocena = 4
elif liczba_pkt >= 80 and liczba_pkt <= 89:
    ocena = 4.5
elif liczba_pkt >= 90 and liczba_pkt <= 100:
    ocena = 5

print("twoja ocena: ", ocena)