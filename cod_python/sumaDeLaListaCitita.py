numere = input("Tastati o serie de numere despartite prin spatiu : ")
suma = 0
numere_split = numere.split(' ')
numarul_de_numere = 0
for nr in numere_split:
    try:
        nr_float = float(nr)
        suma += nr_float
        numarul_de_numere += 1
    except:
        pass

medie = suma / numarul_de_numere
print(f"Suma : {suma}\nMedie : {medie}")