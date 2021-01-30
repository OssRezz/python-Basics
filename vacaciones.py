print("=======================")
print("=Bienvenido a RapiSoft=")
print("=======================")
print("Este sistema determinara los dias de vacaciones")

nombre = input("Ingrese el nombre del titular: ")
claveDepar = int(input("Ingrese la clave del departamento: "))
antiguedad = int(input("Ingrese la antiguedad del titular: "))


if claveDepar == 1 and antiguedad <= 1 :
    print("El titular: " + nombre + " tiene 6 dias de vacaciones")
elif claveDepar == 1 and antiguedad <= 6 :
    print("El titular: " + nombre + " tiene 14 dias de vacaciones")
elif claveDepar == 1 and antiguedad >= 7 :
    print("El titular: " + nombre + " tiene 20 dias de vacaciones")
    
elif claveDepar == 2 and antiguedad <= 1 :
    print("El titular: " + nombre + " tiene 7 dias de vacaciones")
elif claveDepar == 2 and antiguedad <= 6 :
    print("El titular: " + nombre + " tiene 15 dias de vacaciones")
elif claveDepar == 2 and antiguedad >= 7 :
    print("El titular: " + nombre + " tiene 22 dias de vacaciones")

elif claveDepar == 3 and antiguedad <= 1 :
    print("El titular: " + nombre + " tiene 10 dias de vacaciones")
elif claveDepar == 3 and antiguedad <= 6 :
    print("El titular: " + nombre + " tiene 22 dias de vacaciones")
elif claveDepar == 3 and antiguedad >= 7 :
    print("El titular: " + nombre + ", tiene 30 dias de vacaciones")
else :
    print("El codigo no existe.")
