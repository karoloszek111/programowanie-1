print("podaj liczbe studentow: ")
l_studentow = int(input())
zaliczenie = 0
punkty=[]

for student in range(l_studentow):
    print("podaj nazwisko: ")
    nazwisko = input()
    print("podaj liczbe punktow: ") 
    l_punktow = float(input())
    punkty.append(l_punktow)

    if l_punktow < 0 or l_punktow > 100:
        print("blad")
        continue

    if l_punktow >= 0 and l_punktow <= 49:
        ocena = 2
    elif l_punktow >= 50 and l_punktow <= 59:
        ocena = 3
    elif l_punktow >= 60 and l_punktow <= 69:
        ocena = 3.5
    elif l_punktow >= 70 and l_punktow <= 79:
        ocena = 4
    elif l_punktow >= 80 and l_punktow <= 89:
        ocena = 4.5
    elif l_punktow >= 90 and l_punktow <= 100:
        ocena = 5
    if ocena >= 3:
        zaliczenie += 1
    print("student: ",nazwisko, ";liczba punktow: ", l_punktow, ";twoja ocena: ", ocena)
    
print("liczba studentow z zaliczeniem: ", zaliczenie)

srednia = round(sum(punkty)/len(punkty), 2)
print(f"srednia punktow: {srednia}")
print(f"najwieksza ilosc punktow: {max(punkty)}, najmniejsza ilosc punktow: {min(punkty)}")
print(sorted(punkty))
