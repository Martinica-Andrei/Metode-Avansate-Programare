def estePar(n):
    if n % 2 == 0:
        return True
    return False

n = int(input("n : "))

if estePar(n):
    print(f"Numarul {n} este par")
else:
    print(f"Numarul {n} este impar")