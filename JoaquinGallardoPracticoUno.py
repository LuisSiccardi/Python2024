numeros = []
for i in range(10):
    numero = int(input(f"introduce el numero{i+1}: "))
    numeros.append(numero)

numero_pares = [num for num in numeros if num % 2==0]
    
print("numeros pares: ", numero_pares)
