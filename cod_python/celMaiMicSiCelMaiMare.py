numere = input("Tastati o serie de numere despartite prin spatiu : ")
cel_mai_mic = float("inf")
cel_mai_mare = -float("inf")
numere_split = numere.split(' ')
for nr in numere_split:
    try:
        nr_float = float(nr)
        if nr_float > cel_mai_mare:
            cel_mai_mare = nr_float
        if nr_float < cel_mai_mic:
            cel_mai_mic = nr_float
    except:
        pass

print(f"Cel mai mare numar : {cel_mai_mare}\nCel mai mic numar este : {cel_mai_mic}")