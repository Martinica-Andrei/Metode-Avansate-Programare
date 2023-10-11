def iaSumaNumerelor(n):
    suma = 0
    for i in range(1, n  + 1):
        suma += i
    return suma
    #return (n * (n + 1)) / 2

print(f'Suma numerelor pana la 100 : {iaSumaNumerelor(100)}')
