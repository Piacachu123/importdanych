licznik = 0
with open("slowa.txt") as f:
    for line in f:
        if line.strip() == "kot":
            licznik +=1

print(licznik)