l_pomiarow = int(input("podaj liczbe pomiarów: "))
pomiary = []

for _ in range(l_pomiarow):
    pomiar = float(input())
    pomiary.append(pomiar)

print("\npierwszy pomiar: ",pomiary[0], "\ndrugi pomiar: ",pomiary[-1])

if len(pomiary) >= 3:
    print("\ntrzy pierwsze pomiary: ",pomiary[0:3])
else:
    print("\nwszystkie pomiary: ",pomiary)

print("\nco drugi pomiar: ", pomiary[::2])

print("\nw odwrotnej kolejnosci: ", pomiary[::-1])

kopia = pomiary.copy()
kopia[0] = 0
print(pomiary)
print(kopia)