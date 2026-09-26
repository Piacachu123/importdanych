oceny = []
with open("oceny.txt") as f:
    for line in f:
        oceny.append(int(line))
srednia = sum(oceny)/len(oceny)
licznik = 0
for ocena in oceny:
    if ocena > srednia:
        licznik +=1+
print(f"średnia to {srednia}")
print(f"Ocen wikeszych niz srednia jest {licznik}")















#inny sposob
##ile_ocen = 0
##suma =0
##powyzejsr = 0
##with open("oceny.txt") as f:
   ## for line in f:
    ##    suma += int(line.strip())
  ##      ile_ocen+=1

##print(f"średnia to {suma/ile_ocen}")
