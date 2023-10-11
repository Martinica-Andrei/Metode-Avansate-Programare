def sumaNumerelorImpare(n):
    suma = 0
    for i in range(1, n * 2 + 1, 2):
        suma += i
    return suma

print(f"Suma primelor 20 numere impare este : {sumaNumerelorImpare(20)}")