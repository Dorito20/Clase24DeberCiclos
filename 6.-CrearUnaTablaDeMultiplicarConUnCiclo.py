#Modifica el código para generar la tabla de multiplicar del número que el usuario elija.

numero = int(input("Ingrese el número para generar la tabla de multiplicar: "))
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1
