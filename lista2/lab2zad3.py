napoje = ["Woda", "Sok", "Cola"]
ceny = [3, 5, 6]
koszt_zakupow = 0
wybor = 999

print("1. Woda - 3 zl; 2. Sok - 5 zl; 3. Cola - 6 zl; 0. Zakoncz")

while wybor != 0:
    print("wybierz opcje:")
    wybor = int(input())
    if wybor > 0 and wybor <= 3:
        print(f"wybrano: {napoje[wybor - 1]} cena: {ceny[wybor-1]}")
        koszt_zakupow += ceny[wybor-1]
    if wybor < 0 or wybor > 3:
        print("blad, wybor poza zakresem")
print(f"koszt zakupow: {koszt_zakupow}")