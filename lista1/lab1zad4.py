print("podaj wiek: ")
wiek = int(input())
print("czy posiadasz zgode opiekuna?(tak/nie): ")
if input() == "tak":
    zgoda = True
else:
    zgoda = False

print("czy posiadasz dokument tozsamosci?(tak/nie): ")
if input() == "tak":
    dokument = True
else:
    dokument = False

if not dokument:
    print("wypozyczenie niemozliwe")
else:
    if wiek >= 18:
        print("wypozyczenie mozliwe")
    elif wiek >= 13 and wiek <18:
        if zgoda:
            print("wypozyczenie mozliwe")
    else:
        print("wypozyczenie niemozliwe")
