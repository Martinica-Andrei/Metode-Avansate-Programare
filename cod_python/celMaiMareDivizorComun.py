def celMaiMareDivizorComun(a, b):
    while True:
        if a <= 0:
         return b
        if b <= 0:
         return a
        if a >= b:
           a %= b
        else:
           b %= a

a = int(input("a : "))
b = int(input("b : "))
print(f"Cel mai mare divizor comun intre {a} si {b} este {celMaiMareDivizorComun(a, b)}")