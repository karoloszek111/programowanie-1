import pandas as pd

produkt = ["mysz", "monitor", "pc"]
cena = [50, 600, 2000]
ilosc = [35, 25, 10]

df = pd.DataFrame({
"Produkt": produkt,
"Cena": cena,
"Ilosc": ilosc
})

df['Wartosc'] = df['Cena'] * df['Ilosc']
print(df, "\n\n\n")

powyzej_100 = df[df['Cena'] > 100]
print(powyzej_100)

laczna_wartosc = df["Wartosc"].sum()
srednia_cena = df["Cena"].mean()
print(f"laczna wartosc magazynu: {laczna_wartosc}")
print(f"srednia cena: {srednia_cena}")