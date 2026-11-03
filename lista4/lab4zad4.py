
warsztat_python = set()
warsztat_ai = set()
while True:
    print("1 – zapisz na Python,  \
    \n2 – zapisz na AI, \
    \n3 – wyświetl uczestników,\
    \n4 – uczestnicy obu warsztatów, \
    \n5 – wszyscy unikalni uczestnicy, \
    \n0 – zakończ.\
    \nWYBIERZ OPCJE:")
    opcja = int(input())

    if opcja == 1:
        imie = input("podaj imie: ")
        nazwisko = input("podaj nazwisko: ")
        dane = (imie, nazwisko)
        warsztat_python.add(dane)
    elif opcja == 2:
        imie = input("podaj imie: ")
        nazwisko = input("podaj nazwisko: ")
        dane = (imie, nazwisko)
        warsztat_ai.add(dane)
    elif opcja == 3:
        print("wszyscy uczestnicy: ", warsztat_python, warsztat_ai)
    elif opcja == 4:
            print("wspolni uczestnicy: ", warsztat_python & warsztat_ai)
    elif opcja == 5:
        print("unikalni uczestnicy: ", set(warsztat_python | warsztat_ai))
    elif opcja == 0:
        break
    else:
         print("nieprawidlowy wybor opcji")
    