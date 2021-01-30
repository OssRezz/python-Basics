print("Sistema para calcular el promedio de un alumno.")

#Solicitamos la informacion
nombre = input("Para comenzar, ingrese su nombre: ")
Java = float(input("ingrese su nota de la materia Java: "))
visualbasic = float(input("ingrese su nota de la materia Visual Basic: "))
javaScript = float(input("ingrese su nota de la materia JavaScript: "))

#Realizamos los calculos
promedio = ((Java + visualbasic + javaScript) / 3)

#Condicional para aprobar el curso                   
if promedio >= 7 :
    print("Aprobaste el curso, tu promedio es mayor a 7 : ", round(promedio,2))
else :
    print("Eres un fracaso para la humanidad: ", round(promedio,2))
                   
print("Fin.")


