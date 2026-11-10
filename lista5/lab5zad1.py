import numpy as np


l_pomiarow = int(input("podaj liczbe pomiarów: "))
pomiary = np.array([])

for _ in range(l_pomiarow):
    pomiar = float(input())
    pomiary = np.append(pomiary, pomiar)

print(f"srednia: {np.mean(pomiary)}")
print(f"najmnieszy pomiar: {np.min(pomiary)}")
print(f"najwiieszy pomiar: {np.max(pomiary)}")
print(f"rozstep: {np.max(pomiary) - np.min(pomiary)}")