menu = """
***************************************
*1- Introducir notas de matematicas   *
*2- Salir                             *              
***************************************
"""
notas = []
contador = 0
while True:
    print(menu)
    opcion = int(input("Ingrese una de las opciones: "))
    opcion == 1
    nota = int(input(f"introduce las notas de matematicas: "))
    
    if nota > 0 and nota < 11:
        notas.append(nota)
        contador = contador + 1
    for contador in notas():
        promedio = notas + contador
    print(f"El promedio de las notas es:{promedio}")

    opcion == 2
    print("No has ingresado ninguna nota")
    print(menu)



