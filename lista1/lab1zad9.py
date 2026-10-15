print("podaj poczatek zakresu: ")
poczatek = int(input())

print("podaj koniec zakresu: ")
koniec = int(input())

ilosc_p = 0
for x in range(poczatek, koniec + 1):
    if x%2==0:
        print(x, " - parzysta")
        ilosc_p += 1
    else:
        print(x, " - nieparzysta")

print("znaleziono parzystych: ", ilosc_p)