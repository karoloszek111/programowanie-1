while True:
    print("========== KALKULATOR ==========\
    1. Dodawanie\
    2. Odejmowanie\
    3. Mnozenie\
    4. Dzielenie\
    5. Potegowanie\
    6. Srednia z podanych liczb\
    0. Zakoncz\
    ================================")

    print("wybierz opcje:")
    wybor = input()

    if wybor.isdigit():
        wybor = int(wybor)
        while wybor < 0 or wybor > 6:
            print("wybor poza zakresem, wybierz ponownie: ")
            wybor = int(input())
        if wybor == 1:
            print("podaj dwie liczby do dodania: ")
            l1 = float(input())
            l2 = float(input())
            print(l1+l2)

        elif wybor == 2:
            print("podaj dwie liczby do odejmowania: ")
            l1 = float(input())
            l2 = float(input())
            print(l1-l2)

        elif wybor == 3:
                print("podaj dwie liczby do mnozenia: ")
                l1 = float(input())
                l2 = float(input())
                print(l1*l2)

        elif wybor == 4:
                print("podaj dwie liczby do dzielenia: ")
                l1 = float(input())
                l2 = float(input())
                while l2 == 0:
                    print("nie mozna dzielic przez 0 podaj inną liczbę: ")
                    l2 = float(input())
                print(l1/l2)

        elif wybor == 5:
                        print("podaj liczbe i jej potege: ")
                        l1 = float(input())
                        l2 = float(input())
                        print(l1**l2)

        elif wybor == 6:
            print("ile liczb? : ")
            ile_liczb = int(input())
            wynik = 0
            for _ in range(ile_liczb):
                wynik += float(input())
            print(wynik/ile_liczb)

        elif wybor == 0:
             break
        
    else:
         print("bląd wybor nie jest liczbą")
         break