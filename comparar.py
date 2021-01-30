print("Introduce dos numeros a comparar: ")
print("================================")
numero1 = int(input("Cual es el numero que deseas comparar?: " ))
numero2 = int(input("Cual es el numero que deseas comparar?: " ))

if numero1 == numero2 :
    print("Los numeros son iguales")
    if numero1 > numero2 :
        print("El " +  str(numero1) + " es mayor")
    elif numero2 > numero1 :
        print("El " +  str(numero2) + " es mayor")
else :
    print("Los numeros no son iguales")
    if numero1 > numero2 :
        print("El " +  str(numero1) + " es mayor")
    elif numero2 > numero1 :
        print("El " +  str(numero2) + " es mayor")
