wydatki = []
stan_konta = 0
nr_operacji = 0
while True:
    print("========= MOJ BUDZET =========\
    1. Dodaj przychod\
    2. Dodaj wydatek\
    3. Wyswietl historie operacji\
    4. Wyswietl stan konta\
    5. Podsumowanie finansowe\
    6. Usun operacje\
    0. Zakoncz\
    ==============================")
    print("wybierz opcje: ")
    wybor = int(input())
    while wybor < 0 or wybor > 6:
        print("wybor poza zakresem wybierz ponownie: ")
        wybor = int(input())

    if wybor == 1:
        print("opis: ")
        opis = input()
        print("kwota: ")
        kwota = float(input())
        while kwota < 0:
            print("kwota nie moze byc mniejsza od 0 podaj ponownie: ")
            kwota = float(input())
        wydatki.append({nr_operacji:[opis, kwota, "przychod"]})
        nr_operacji += 1

        stan_konta += kwota

    elif wybor == 2:
        print("opis: ")
        opis = input()
        print("kwota: ")
        kwota = float(input())
        while kwota < 0:
                    print("kwota nie moze byc mniejsza od 0 podaj ponownie: ")
                    kwota = float(input())
        wydatki.append({nr_operacji:[opis, kwota, "wydatek"]})
        nr_operacji += 1

        stan_konta -= kwota

    elif wybor == 3:
        if wydatki == []:
             print("pusta historia")
        else:
            print(wydatki)

    elif wybor == 4:
        print(f"stan konta: {stan_konta}")

    elif wybor == 5:
        s_przychod = 0
        s_wydatki = 0
        max_win = 0
        nr = 0
        for x in wydatki:
            if x[nr][2] == "przychod":
                s_przychod += x[nr][1]
            elif x[nr][2] == "wydatek":
                s_wydatki += x[nr][1]
                if x[nr][1] > max_win:
                    max_win = x[nr][1]
            nr += 1

        print(f"suma przychodow: {s_przychod}")
        print(f"suma wydatkow: {s_wydatki}")
        print(f"bilans: {stan_konta}")
        if max_win == 0:
            print("brak wydatkow")
        else:
            print(f"najwiekszy wydatek: {max_win}")

    elif wybor == 6:
        usun = int(input("podaj transakcje do usuniecia:"))
        if wydatki[usun][usun][2] == "przychod":
            stan_konta -= wydatki[usun][usun][1]
        elif wydatki[usun][usun][2] == "wydatek":
                    stan_konta += wydatki[usun][usun][1]
        wydatki.pop(usun)

    elif wybor == 0:
         break

