zadania = []
print("1 – Dodaj zadanie,\
• 2 – Wyświetl zadania,\
• 3 – Usuń zadanie,\
• 4 – Wyświetl liczbę zadań,\
• 0 – Zakończ.)")

wybor = 999
while wybor != 0:
    print("wybierz opcje:")
    wybor = int(input())

    if wybor == 1:
        print("podaj nazwe zadania:")
        zadanie = input()
        zadania.append(zadanie)

    elif wybor == 2:
        for z in range(len(zadania)):
            print(f"{z + 1}. {zadania[z]}")

    elif wybor == 3:
        print(f"podaj numer zadania do usuniecia w zakresie (1 do {len(zadania)})")
        numer = int(input())
        while numer < 1 or numer > len(zadania):
            print("bledny numer zadania podaj ponownie:")
            numer = int(input())
        zadania.pop(numer-1)

    elif wybor == 4:
        if len(zadania) == 0:
            print("pusta lista zadan")
        print(f"liczba aktualnych zadan: {len(zadania)}")

    elif wybor < 0 or wybor > 4:
        print("bledny wybor podaj ponownie:")
        continue
    