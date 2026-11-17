import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("klienci.csv", encoding="utf-8-sig")
print(df.columns)
print(f"liczba klientow {len(df['klient'])}")

df = df[["klient", "miasto", "wojewodztwo", "zamowienia"]]

df_posortowane = df.sort_values(by="zamowienia", ascending=False)

top5 = df_posortowane.head(5)[['klient', 'miasto', 'zamowienia']]
print(top5)

suma_zamowien = df['zamowienia'].sum()
print(f"suma zamowien: {suma_zamowien}")

df_posortowane['udzial_procent'] = (df_posortowane['zamowienia'] / suma_zamowien) * 100
print(df_posortowane.head(5))

suma_top10 = df_posortowane.head(10)["zamowienia"].sum()
suma_pozostali = suma_zamowien - suma_top10
procent_10 = df_posortowane.head(10)["udzial_procent"].sum()

print(f"[Odp.a] Który klient zamówił najwięcej sztuk? {df_posortowane.iloc[0]['klient']}")
print(f"[Odp.b] Jaki procent wszystkich zamówionych sztuk pochodzi od 10 największych klientów? {procent_10}")

plt.figure(figsize=(10, 6))
plt.barh(df_posortowane.head(10)["klient"].astype(str), df_posortowane.head(10)["zamowienia"])
plt.xlabel("klient")
plt.ylabel("zamowienia")
plt.title("10 klientow z najwieksza liczba zamowien")
plt.show()

plt.figure(figsize=(7,7))
plt.pie([suma_top10, suma_pozostali],labels=["TOP 10 klientów", "Pozostali klienci"], autopct='%1.1f%%')
plt.title("Udział TOP 10 klientów w całkowitej liczbie zamówionych sztuk")
plt.show()