haslo = "Python123"
podane_haslo = ""
l_prob = 0

while True:
    if l_prob == 3:
        print("konto zablokowane")
        break

    l_prob += 1
    
    print("podaj haslo:")
    podane_haslo = input()
    if podane_haslo == haslo:
        print("logowanie udane")
        break
    else:
        print(f"bledne haslo, pozostale proby: {3 - l_prob}")