cena_produktu = int(input())
liczba_produktow = int(input())

wartosc_produktow = cena_produktu * liczba_produktow
do_zaplaty = 0

if wartosc_produktow >= 100:
    koszt_dostawy = 0
else:
    koszt_dostawy = 12

do_zaplaty = wartosc_produktow + koszt_dostawy

print("wartosc produktow: ", wartosc_produktow, "\n koszt dostawy:", koszt_dostawy, "\n do zaplaty:", do_zaplaty)