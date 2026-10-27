ksiazki = {}
numery = 1

while True:
    print("========== BIBLIOTEKA ==========\
    1. Dodaj ksiazke\
    2. Wyswietl wszystkie ksiazki\
    3. Wypozycz ksiazke\
    4. Zwroc ksiazke\
    5. Usun ksiazke\
    0. Zakoncz\
    ===============================")

    print("wybierz opcje:")
    wybor = int(input())
    if wybor == 1:
        print("podaj tytuł: ")
        tytul = input()
        print("podaj autora: ")
        autor = input()
        ksiazki[numery] = [tytul, autor, "dostępny"]
        numery += 1

    elif wybor == 2:
        print(ksiazki)

    elif wybor == 3:
        print("podaj numer ksiazki która chcesz wypozyczyc:")
        wyp = int(input())
        if ksiazki[wyp][2] == "dostępny":
            print("wypozyczono")
            ksiazki[wyp][2] = "niedostępny"
        else:
            print("ksiazka niedostepna")

    elif wybor == 4:
        print("podaj numer ksiazki która chcesz oddac:")
        wyp = int(input())
        if ksiazki[wyp][2] == "niedostępny":
            print("oddano")
            ksiazki[wyp][2] = "dostępny"
        else:
            print("ksiazka nie zostala wypozyczona")

    elif wybor == 5:
        print("podaj numer ksiazki do usuniecia: ")
        usun = int(input())
        ksiazki.pop(usun)

    elif wybor == 0:
        break