l_pomiarow = int(input("podaj liczbe pomiarow: "))
pomiary = []
prog_alarmowy = 50

for _ in range(l_pomiarow):
    pomiar = float(input("podaj kolejny pomiar: "))
    pomiary.append(pomiar)

pomiary2 = [x for x in pomiary if x<prog_alarmowy]
print("pomiary alarmowe: ",pomiary2)

podwojone = [x * 2 for x in pomiary]
print("pomiary podwojone: ", podwojone)
print("czy chociaz jeden przekracza prog?: ","tak" if any(x > prog_alarmowy for x in pomiary) else "nie")
print("czy wszystkie nie przekraczaja progu?: ", "tak" if all(x <= prog_alarmowy for x in pomiary) else "nie")
