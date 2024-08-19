menu = """
******************************************
*1- Introducir notas de matematicas      *
*2- Mostrar promedio y cantidad de notas *   
*3- Salir                                *              
******************************************
"""

notas = []
contador = 0

while True:
    print(menu)
    opcion = int(input("Ingrese una de las opciones: "))
    if opcion == 1:
        nota = int(input(f"introduce las notas de matematicas: "))
        if 0 < nota < 11: #nota > 0 and nota < 11
            notas.append(nota)
            contador = contador + 1
        else:
            print("No es un valor válido")
            continue

    if opcion == 2:
        for contador in notas():
            promedio = (notas + 0)/contador #notas + contador
            print(f"El promedio de las notas es:{promedio}")
        print(notas)

    if opcion == 3:
       print("Nos vemo, chau")
       break
    
print("FIN")
       # print("No has ingresado ninguna nota")
       # print(menu)



