liczba = 0
with open("liczby.txt") as f:
    for linia in f:
        linia = (linia.strip())
        liczba += int(linia)

print(liczba)