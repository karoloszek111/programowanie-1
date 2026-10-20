temperatury = []
for x in range(7):
    print(f"dzien {x+1}")
    temp = float(input())
    temperatury.append(temp)

avg_temp = round(sum(temperatury) / len(temperatury), 2)
max_temp = max(temperatury)
min_temp = min(temperatury)

powyzej_sredniej = []

for t in temperatury:
    if t > avg_temp:
        powyzej_sredniej.append(t)

print(f"srednia temperatura: {avg_temp}, maksymalna temperatura: {max_temp}, najmniejsza temperatura: {min_temp}")
print(f"dni powyzej sredniej: {powyzej_sredniej}, liczba dni: {len(powyzej_sredniej)}")