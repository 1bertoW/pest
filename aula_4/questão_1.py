numero = int(input("Digite um número inteiro: "))

if numero == 0:
    resultado = "neutro"
    print("zero")
elif numero % 2 == 0:
    pares = numero
    resultado = "par"
    print("par")
else:
    impares = numero
    resultado = "ímpar"
    print("impar")
