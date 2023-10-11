def esteAnBisect(n):
    if abs(n) % 4 == 0:
        return True
    return False

an = int(input("An : "))

if esteAnBisect(an):
    print (f"Anul {an} este an bisect")
else:
    print(f"Anul {an} nu este an bisect")