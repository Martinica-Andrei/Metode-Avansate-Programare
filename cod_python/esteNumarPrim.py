import math
def esteNumarPrim(n):
    if n <= 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 2): # +2 sa fie sigur ca merge
        if n % i == 0:
            return False
        
    return True

x = int(input("x : "))
if esteNumarPrim(x):
    print(f"Numarul {x} este prim")
else:
    print(f"Numarul {x} nu este prim")
