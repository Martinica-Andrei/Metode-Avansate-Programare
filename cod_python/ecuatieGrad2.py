import math
a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))
print(f"Ecuatie : {a}x^2 + {b}x + {c} ")
epsilon = 1e-09

if abs(a) <= epsilon: # verificare a == 0 dar pentru ca e float verificam daca e aproape de 0 , la fel pentru celelalte
    if abs(b) <= epsilon:
        if abs(c) <= epsilon:
            print("Orice x este solutie")
        else:
            print("Nu exista nicio solutie")
    else:
        print(f"Solutia este {-c/b}")
else:
    delta = b ** 2 - 4 * a * c
    if abs(delta) <= epsilon:
        print(f"Solutia ecuatiei este {-b / (2 * a)}")
    elif delta < 0:
        print("Nu exista nicio solutie")
    else:
        sqrt_delta = math.sqrt(delta)
        x_1 = (-b + sqrt_delta) / (2 * a)
        x_2 = (-b - sqrt_delta) / (2 * a)
        print(f"Solutiile ecuatiei sunt : {x_1} si {x_2}")