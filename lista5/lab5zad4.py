import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def oblicz_ocene(punkty):
    if punkty < 50:
        return 2.0
    elif punkty < 60:
        return 3.0
    elif punkty < 70:
        return 3.5
    elif punkty < 80:
        return 4.0
    elif punkty < 90:
        return 4.5
    else:
        return 5.0


print("podaj liczbe studentow: ")
l_studentow = int(input())
zaliczenie = 0
punkty=[]
nazwiska = []
oceny = []


for student in range(l_studentow):
    print("podaj nazwisko: ")
    nazwisko = input()
    nazwiska.append(nazwisko)
    print("podaj liczbe punktow: ") 
    l_punktow = float(input())

    if l_punktow < 0 or l_punktow > 100:
        print("blad")
        continue
    else:
        punkty.append(l_punktow)

    print("student: ",nazwisko, ";liczba punktow: ", l_punktow)

df = pd.DataFrame({
"Nazwiska": nazwiska,
"Punkty": punkty,
})
df["Oceny"] = df["Punkty"].apply(oblicz_ocene)

print(df.sort_values("Punkty", ascending=False), "\n\n\n")

srednia = df["Oceny"].mean()
print(f"srednia ocena: {srednia}")
zaliczenia = (df["Oceny"] >= 3.0).sum()
print(f"zaliczenia: {zaliczenia}")


plt.bar(df["Nazwiska"], df["Oceny"])
plt.title("Wyniki egzaminu")
plt.xlabel("Student")
plt.ylabel("Ocena")
plt.ylim(0, 5.5)
plt.show()