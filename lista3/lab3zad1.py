kontakty = {}

while True:
    print("========== KSIAZKA KONTAKTOW ==========\
    1. Dodaj kontakt\
    2. Wyswietl wszystkie kontakty\
    3. Wyszukaj kontakt\
    4. Edytuj kontakt\
    5. Usun kontakt\
    0. Zakoncz\
    =======================================")

    print("wybierz opcje:")
    wybor = int(input())

    if wybor == 1:
        print("imie: ")
        imie = input()
        print("nazwisko: ")
        nazwisko = input()
        print("telefon: ")
        telefon = input()
        kontakty[telefon] = [imie, nazwisko]

    elif wybor == 2:
        if kontakty == {}:
            print("pusta ksiazka kontaktow")
        else:
            print(kontakty)

    elif wybor == 3:
        print("podaj numer szukanego kontaktu: ")
        numer = input()
        print(kontakty[numer])

    elif wybor == 4:
        print("podaj numer kontaktu do zmiany: ")
        numer = input()
        print("podaj nowe imie i nazwisko: ")
        imie = input()
        nazwisko = input()
        kontakty[numer] = [imie, nazwisko]

    elif wybor == 5:
        print("podaj numer kontaktu do usuniecia: ")
        numer = input()
        kontakty.pop(numer)

    elif wybor == 0:
        break
    