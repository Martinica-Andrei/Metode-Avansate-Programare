def produsulNumerelorNaturale(n):
    if n <= 0:
        return 0
    produs = 1
    for i in range(2, n + 1):
        produs *= i
    return produs

print(f'Produsul primelor 10 numere naturale {produsulNumerelorNaturale(10)}')