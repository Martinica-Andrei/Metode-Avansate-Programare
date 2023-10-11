a = float(input("Primul unghi : "))
b = float(input("Al doilea unghi : "))
c = float(input("Al treilea unghi : "))
epsilon = 1e-09

if abs(a + b + c - 180) < epsilon:
    print("Aceste unghiuri pot forma un triunghi.")
else:
    print("Aceste unghiuri nu pot forma un triunghi")