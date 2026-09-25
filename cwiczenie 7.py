licznik_wieczorzimno = 0
stala = 0
licznik_ponizejzera = 0
with open("pomiary.txt") as f:
    for line in f:
        miasto ,temp1, temp2 = line.split()
        temp1,temp2 = int(temp1),int(temp2)
        zmianatemp = temp2-temp1
        print(f"{miasto} zmiana temp to {zmianatemp}")
        if temp1 < stala:
            stala = temp1
            miasto_najnizszatemp = miasto
        if temp1 > temp2:
            licznik_wieczorzimno += 1
        if temp1<0 and temp2 < 0:
            licznik_ponizejzera+=1
print(f"Najnizsza temperature ma {miasto_najnizszatemp}")

print(f"W {licznik_wieczorzimno} bylo zimniej wiczorem niz rano")

print(f"W {licznik_ponizejzera} bylo zarowno rano jak wieczorem ponizej zera")