def factorial(n):
    if n < 0:
        return 0
    produs = 1
    for i in range(2, n + 1):
        produs *= i
    return produs

x = int(input("x : "))
print(f"!{x} = {factorial(x)}")