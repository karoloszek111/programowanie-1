import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("magazyny.csv", encoding="utf-8-sig")
print(df.columns)
print(df.head)

df = df[['magazyn', 'miasto', 'wojewodztwo', 'produkty']]

print(f"Liczba magazynow: {len(df)}")
df_posortowane = df.sort_values(by="produkty",ascending=False)

top5 = df_posortowane.head(5)[["magazyn", "miasto", "produkty"]]
top10 = df_posortowane.head(10).iloc[::-1]
print(top5)

suma_p = df['produkty'].sum()
print(f"łączna liczba produktow: {suma_p}")

najwiekszy = top5.iloc[0]
piaty = top5.iloc[4]
roznica_1_5 = najwiekszy["produkty"] - piaty["produkty"]
print(f"[Odp.a] magazyn z najwieksza iloscia produktow: {najwiekszy['magazyn']}, ma produktow: {najwiekszy['produkty']}")
print(f"[Odp.b] roznica miedzy pierwszym a piatym magazynem {roznica_1_5}")

plt.figure(figsize=(10, 6))
plt.barh(top10["magazyn"].astype(str), top10["produkty"])
plt.xlabel("Liczba produktów")
plt.ylabel("Identyfikator magazynu")
plt.title("10 magazynów z największą liczbą produktów")
plt.show()
