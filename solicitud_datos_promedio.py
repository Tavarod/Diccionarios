empleados = {}

while True:
    # Pedir información del empleado
    codigo = input("Ingrese el código del empleado: ")
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: ")) # Convertir la entrada de edad a un número entero
    salario = input("Ingrese salario del empleado")
    sexo = input("Genero de nacimiento")

    # Agregar información del empleado al diccionario
    empleados[codigo] = {"nombre": nombre, "edad": edad, "salario":salario, "sexo": sexo}

    # Preguntar si desea agregar otro empleado
    respuesta = input("¿Desea agregar otro empleado? (s/n): ")
    if respuesta.lower() == "n":
        break

# Imprimir el diccionario con todos los empleados
print(empleados)

# Calcular el promedio de edad de todos los empleados
total_edad = 0
for empleado in empleados.values():
    total_edad += empleado["edad"]
promedio_edad = total_edad / len(empleados)

# Imprimir el promedio de edad
print("El promedio de edad de todos los empleados es:", promedio_edad)

"""
Se a convertido la entrada de edad en un número entero usando la función int(), y también he agregado 
na variable total_edad para ir sumando todas las edades mientras se recorre el diccionario. 
Luego, he dividido total_edad por el número de empleados en el diccionario para obtener el promedio de edad.
El método .values() se utiliza en este código para obtener todos los valores del diccionario "empleados". 
En otras palabras, devuelve una lista de todos los valores de cada clave en el diccionario. 
En este caso, devuelve una lista de todos los diccionarios con la información de cada empleado.
En resumen, .values() es útil para obtener una lista de todos los valores de un diccionario sin necesidad 
de conocer sus claves.
"""