import math
lepszy_skoklista = []
suma_lepszychskokow = 0
ilosc_lepszychskokow = 0
lczinik_powyzejsr = 0
temp = math.inf
with open("zawodnicy.txt") as f:
    for line in f:
        imie,kraj,skok1,skok2 = line.split()
        skok1,skok2 = int(skok1), int(skok2)

        if skok1 > skok2:
            lepszy_skok = skok1
        if skok2>skok1:
            lepszy_skok = skok2
        if skok1==skok2:
            lepszy_skok = skok1
        lepszy_skoklista.append(lepszy_skok)
        if skok2<temp:
            temp=skok2
            krajtemp = kraj
        suma_lepszychskokow+=lepszy_skok
        ilosc_lepszychskokow +=1
        print(f"{imie} lepszy skok wynosil {lepszy_skok}")
for skok in lepszy_skoklista:
    if skok>suma_lepszychskokow/ilosc_lepszychskokow:
        lczinik_powyzejsr += 1
print(f"Średnia z lepszych skokow to {suma_lepszychskokow/ilosc_lepszychskokow}")
print(f"Najmniejszy drugi skok miał {krajtemp} i wynosil {temp}")
print(f"Skokow powyzej srednie bylo {lczinik_powyzejsr}")