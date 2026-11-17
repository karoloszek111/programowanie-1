import pandas as pd
import matplotlib.pyplot as plt

df_kli = pd.read_csv("klienci.csv", encoding="utf-8-sig")
df_mag = pd.read_csv("magazyny.csv", encoding="utf-8-sig")

df_mag = df_mag[['wojewodztwo', 'produkty']]
df_kli = df_kli[['wojewodztwo', 'zamowienia']]

mag_woj = df_mag.groupby("wojewodztwo", as_index=False)["produkty"].sum()
kli_woj = df_kli.groupby("wojewodztwo", as_index=False)["zamowienia"].sum()

print(mag_woj, '\n\n\n\n', kli_woj)

df_merged = pd.merge(mag_woj, kli_woj, on="wojewodztwo").fillna(0)
print(df_merged)

df_merged['roznica'] = df_merged['produkty']-df_merged['zamowienia']
df_merged = df_merged.sort_values(by="roznica", ascending=True)
print(df_merged)

najmniejsza_roznica_woj = df_merged.iloc[0]["wojewodztwo"]
liczba_deficytowych = (df_merged["roznica"] < 0).sum()
print(f"[Odp.a] W którym województwie różnica produkty - zamowienia jest najmniejsza? {najmniejsza_roznica_woj}")
print(f"[Odp.b] W ilu województwach liczba produktów jest mniejsza od liczby zamówionych sztuk? {liczba_deficytowych}")

df_merged.plot(
    x="wojewodztwo",
    y=["produkty", "zamowienia"],
    kind="bar",
    figsize=(12, 6),
    color=["green", "red"]
)
plt.xlabel("Województwo")
plt.ylabel("Liczba sztuk")
plt.title("Porównanie dostępnych produktów i zamówień w województwach")
plt.legend()
plt.show()


plt.figure(figsize=(10, 7))
plt.barh(df_merged["wojewodztwo"], df_merged["roznica"])
plt.xlabel("Różnica (Produkty - Zamówienia)")
plt.ylabel("Województwo")
plt.title("Bilans produktów i zamówień w województwach")
plt.show()