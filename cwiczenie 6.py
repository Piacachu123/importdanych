temp_punkty = 0
imie_punkty = ""
licznik = 0
lczinik_odst = 0
with open("punkty.txt") as f:
    for line in f:
        imie,a,b,c = line.split()
        a,b,c = int(a) , int(b) , int(c)
        suma = int(a) + int(b) + int(c)
        if a >= 50 and b >= 50 and c >= 50:
            licznik+=1
        if suma > temp_punkty:
            temp_punkty = suma
            imie_punkty = imie
        if a >c:
            lczinik_odst+=1
        print(imie, suma)

print(f"najwięcej punktow {imie_punkty}")

print(f"{licznik} ma punkty ponad 50")

print(f"{lczinik_odst} ma wynik wiekszy od ostatniego")