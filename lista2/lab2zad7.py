magazyn = {"Mysz": 5, "Klawiatura": 3, "Monitor": 2}
print("1 – stan magazynu, 2 – przyjęcie towaru, 3 – wydanie towaru, 0\
– zakończenie.")
wybor = 999
while wybor != 0:
    print("wybierz opcje:")
    wybor = int(input())
    if wybor==1:
        for x in magazyn:
            print(f"{x}:{magazyn[x]}")
    elif wybor==2:
        print("podaj produkt:")
        produkt = input()
        print("podaj ilosc:")
        ilosc = int(input())
        if produkt in magazyn:
            magazyn[produkt] += ilosc
        else:
            magazyn[produkt] = ilosc

    elif wybor==3:
            print("podaj produkt:")
            produkt = input()
            print("podaj ilosc:")
            ilosc = int(input())
            if produkt in magazyn:
                if magazyn[produkt] >= ilosc:
                    magazyn[produkt] -= ilosc
                else:
                    print("nie wystarczajaco duzo towaru")
            else:
                print("brak produktu")