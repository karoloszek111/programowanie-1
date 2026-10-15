print("podaj kwote odkladana tygodniowo: ")
kwota = int(input())

print("podaj liczbe tygodni oszczedzania: ")
tygodnie = int(input())

suma= 0
for tydzien in range(tygodnie ):
    suma += kwota
    print("tydzien: ",tydzien + 1, " suma: ", suma)

print("calkowicie zaoszczedzona kwota: ", suma)