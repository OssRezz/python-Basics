print("El numero mayor de los 3")

numero1 = int(input("Ingrese el numero 1: "))
numero2 = int(input("Ingrese el numero 2: "))
numero3 = int(input("Ingrese el numero 3: "))

if numero1 >  numero2 and numero1 >  numero3:
    print("El numero " + str(numero1) + " Es mayor")   
elif numero2 >  numero1 and numero2 >  numero3:
    print("El numero " + str(numero2) + " Es mayor")

elif numero3 >  numero1 and numero3 >  numero2:
    print("El numero " + str(numero3) + " Es mayor")

else :
    print("no hay un numero mayor")
