numero = int(input("Digite um número: "))

pares = -1
impares = -1

if numero != 0:
    if numero % 2 == 0:
        pares = numero
        print(f"Pares: {numero}")
    else:
        impares = numero
        print(f"impares: {numero}")
