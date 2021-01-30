print("Calculadora con una sola variable ")
print("********************")
print("* Menu de opciones *")
print("********************")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Division Entera")
print("6. Exponente")
print("7. Modulo o Residuo \n")


numero = int(input("introduce la opcion deseada: "))

if numero == 1 :
    print("Elegiste Suma \n")
    numero_uno = int(input("Introduce el primer numero: "))
    numero_dos = int(input("Introduce el segundo numero: "))
    numero = numero_uno + numero_dos
    print("El valor de la suma es: ", numero)
    
elif numero == 2 :
    print("Elegiste Resta \n")
    numero_uno = int(input("Introduce el primer numero: "))
    numero_dos = int(input("Introduce el segundo numero: "))
    numero = numero_uno - numero_dos
    print("El valor de la Resta es: ", numero)
    
elif numero == 3 :
    print("Elegiste Multiplicacion \n")
    numero_uno = int(input("Introduce el primer numero: "))
    numero_dos = int(input("Introduce el segundo numero: "))
    numero = numero_uno * numero_dos
    print("El valor de la Multiplicacion es: ", numero)

elif numero == 4 :
    print("Elegiste Division \n")
    numero_uno = float(input("Introduce el primer numero: "))
    numero_dos = float(input("Introduce el segundo numero: "))
    numero = numero_uno / numero_dos
    print("El valor de la Division es: ", numero)

elif numero == 5 :
    print("Elegiste Division Entera \n")
    numero_uno = float(input("Introduce el primer numero: "))
    numero_dos = float(input("Introduce el segundo numero: "))
    numero = numero_uno // numero_dos
    print("El valor de la Division Entera es: ", numero)

elif numero == 6 :
    print("Elegiste Exponente \n")
    numero_uno = float(input("Introduce el primer numero: "))
    numero_dos = float(input("Introduce el segundo numero: "))
    numero = numero_uno ** numero_dos
    print("El valor de la potencia  es: ", numero)
elif numero == 7 :
    print("Elegiste Modulo o Residuo \n")
    numero_uno = int(input("Introduce el primer numero: "))
    numero_dos = int(input("Introduce el segundo numero: "))
    numero = numero_uno % numero_dos
    print("El valor del Residuo  es: ", numero)






