print("podaj wysokosc choinki: ")
wysokosc = int(input())

for i in range(wysokosc):
    odstepy = " " * (wysokosc - i)
    gwiazdki = "*" * (i * 2 + 1)
    print(odstepy + gwiazdki)