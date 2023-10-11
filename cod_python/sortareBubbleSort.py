def sortareBubbleSort(lista):
    # se poate si cu o booleana , un while loop sa verifice daca a dat swap , si un singur for loop
    # dar asa e mai eficient
    # intuitiv la fiecare iteratie i se misca cel mai mare element la indexul len(lista) - i - 1 din 
    # lista 

    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


numere = input("Tastati o serie de numere despartite prin spatiu : ")
numere_split = numere.split(' ')
numere = []
for nr in numere_split:
    try:
        nr_float = float(nr)
        numere.append(nr_float)
    except:
        pass

sortareBubbleSort(numere)
print(numere)