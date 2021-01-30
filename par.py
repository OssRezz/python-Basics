print("*******************************************************")
print("* Este programa determina si un numero es par o impar *")
print("*******************************************************")

numero = int(input("Ingrese un numero: "))
modulo = numero % 2
if modulo == 0 :
    print("Es par")
else :
    print("Es impar")
    
