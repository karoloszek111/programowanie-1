print("podaj cene produktu: ")
cena_produktu = int(input())

print("podaj wartosc rabatu (%): ")
rabat = 1 - (int(input()) / 100)

cena_koncowa = cena_produktu * rabat
kwota_rabat = cena_koncowa - cena_produktu

if rabat <= 0.8:
    print("duza promocja!")
else:
    print("standardowa promocja")

print("cena poczatkowa: ", cena_produktu, "\n", "kwota rabatu: ", kwota_rabat, "\n", "cena koncowa: ", cena_koncowa)