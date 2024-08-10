#Modifica el código para que el usuario pueda ingresar el número del cual desea calcular el factorial.

numero = int(input("Ingrese el número del cual desea calcular el factorial: "))

factorial = 1
for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es:", factorial)
