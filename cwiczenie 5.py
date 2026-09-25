stala = 0
with open("osoby.txt") as f:
    for line in f:
        imie,wiek = (line.split())
        if int(wiek) > stala:
            imie_najstarszy = imie
            stala = int(wiek)
            wiek_najstarszy = int(wiek)
print(imie_najstarszy)
print(wiek_najstarszy)
