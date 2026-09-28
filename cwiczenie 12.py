import math

tablica = []
with open("siatka.txt") as f:
    for line in f:
        wiersz = []
        temp =  -1*math.inf
        for x in line.split():
            x = int(x)
            if x > temp:
                temp = x
            wiersz.append(int(x))
        print(temp)
        tablica.append(wiersz)


    print(tablica)