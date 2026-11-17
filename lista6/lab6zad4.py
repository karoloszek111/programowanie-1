import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("magazyny.csv", encoding="utf-8-sig")
print(df.columns)

df = df[['magazyn', 'miasto', 'wojewodztwo','produkty']]
wojewodztwo = input("podaj wojewodztwo")
min_liczba_produktow = int(input("podaj minimalną liczbe produktow"))

wynik = df[
    (df["wojewodztwo"].str.lower() == wojewodztwo) &
    (df["produkty"] >= min_liczba_produktow)
]

if wynik.empty:
    print("\nNie znaleziono zadnego magazynu spelniajacego podane warunki.")
    print("[Odp. a] Liczba magazynow spelniajacych warunki: 0")
    print("[Odp. b] Brak wynikow - nie mozna wskazac magazynu z najwieksza liczba produktow.")
else:
    wynik_sorted = wynik.sort_values(by="produkty", ascending=False)
    print("\nMagazyny spelniajace warunki:")
    print(wynik_sorted[["magazyn", "miasto", "produkty"]])

    liczba_mag = len(wynik_sorted)
    suma_prod = wynik_sorted["produkty"].sum()
    print(f"\nLiczba magazynow: {liczba_mag}")
    print(f"Suma produktow: {suma_prod}")

    najlepszy_mag = wynik_sorted.iloc[0]["magazyn"]
    print(f"\n[Odp. a] Warunki spelnia {liczba_mag} magazynow.")
    print(f"[Odp. b] Najwiecej produktow sposrod znalezionych ma magazyn: {najlepszy_mag}")

    top_wynik = wynik_sorted.head(5).iloc[::-1]

    plt.figure(figsize=(9, 5))
    plt.barh(top_wynik["magazyn"], top_wynik["produkty"])
    plt.xlabel("Liczba produktów")
    plt.ylabel("Identyfikator magazynu")
    plt.title(f"TOP magazyny w woj. {wojewodztwo} (min. {min_liczba_produktow} szt.)")
    plt.tight_layout()
    plt.show()