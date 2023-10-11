def fibonacci(n):
    a = 0
    b = 1
    rezultat = ""
    for i in range(0, n):
        rezultat += str(a) + " "
        suma = a + b
        a = b
        b = suma
    print(rezultat)

n = int(input("Tastati cate numere vreti sa afisati la secventa fibonacii : "))
fibonacci(n)