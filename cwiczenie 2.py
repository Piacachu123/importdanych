liczba = 0

licznik = 0
with open("liczby.txt") as f:
    for line in f:
        temp = int(line)
        if int(line) >50:
            licznik+=1
        if int(line) > liczba:
            liczba = int(temp)

print(liczba)

print(licznik)