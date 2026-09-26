wartosc = 0
temp_najwieszkawartosc = 0
with open("produkty.txt") as f:
    for line in f:
        produkt,cena,ilosc = line.strip().split(";")
        cena,ilosc = float(cena),float(ilosc)
        print(f"produkt: {produkt} , {cena*ilosc}")
        wartosc+=(cena*ilosc)
        if temp_najwieszkawartosc < (cena*ilosc):
            temp_najwieszkawartosc = cena*ilosc
            temp_produktnajwiekszawrtosc = produkt
print(f"Laczna wartosc produktow to {wartosc}")
print(f"Pordukt o najwiekszej wartosci to {temp_produktnajwiekszawrtosc}")
