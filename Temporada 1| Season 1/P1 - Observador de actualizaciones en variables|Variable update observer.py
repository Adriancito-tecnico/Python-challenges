a = "1"
X = a
while True:
    a = input("Introduzca el valor de a:")
    if a != X:
        print("La variable a ha sido actualizada")
        print(f"Valor antiguo: {X} Valor nuevo: {a}")
        X = a
