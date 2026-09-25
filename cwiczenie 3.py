lczinik =0
with open("pary.txt") as f:
    for line in f:
        a,b = map(int,line.split())
        if a>b:
            lczinik+=1
        print(int(a)+int(b))
print(f"Tyle jest liczb gdzie pierwsza jest wieksz od rugiej : {lczinik}")
