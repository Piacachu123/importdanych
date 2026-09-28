licznikzer = 0
tablica= []
with open("plansza.txt") as f:
    for line in f:
        wiersz = []
        for  x in line.split():
            wiersz.append(int(x))
        tablica.append(wiersz)

    for wiersz in tablica:
        print(sum(wiersz))
        licznikzer+=wiersz.count(0)
print(tablica)

for k in range(5):
    sumakol = 0
    for wiersz in tablica:
        sumakol+=wiersz[k]
    print(sumakol)

print(licznikzer)

























# moj sposob
# suma_kolumny1 = 0
# sumakolumny2 = 0
# sumakolumny3 = 0
# sumakolumny4 = 0
# suma_kolumny5 = 0
# zera_plansza = 0
# with open("plansza.txt") as f:
#     for line in f:
#         a,b,c,d,e = map(int,line.split())
#         print(f"suma wiersza to {a+b+c+d+e}")
#         if a == 0:
#             zera_plansza+=1
#         if b ==0:
#             zera_plansza+=1
#         if c ==0:
#             zera_plansza+=1
#         if d == 0:
#             zera_plansza+=1
#         if e ==0:
#             zera_plansza+=1
#         suma_kolumny1+=a
#         sumakolumny2+=b
#         sumakolumny3+=c
#         sumakolumny4+=d
#         suma_kolumny5+=e
# print(f"Suma kolumny 1 to {suma_kolumny1}")
# print(f"Suma kolumny 2 to {sumakolumny2}")
# print(f"Suma kolumny 3 to {sumakolumny3}")
# print(f"Suma kolumny 4 to {sumakolumny4}")
# print(f"Suma kolumny 5 to {suma_kolumny5}")
# print(f"zer na planszy jest {zera_plansza}")