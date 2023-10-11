zile = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
def convertesteNumarInZi(ziua):
    if ziua <= 0:
        return "invalid, ziua trebuie sa fie mai mare decat 0"
    return zile[(ziua - 1) % 7]

ziua = int(input("Tasteaza un numar intreg incepand de la 1 si afli ziua : "))
print(convertesteNumarInZi(ziua))