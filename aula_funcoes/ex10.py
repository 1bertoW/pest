# Escreva um programa que contenha uma função chamada calcular_perimetro que receba o lado de um quadrado como parâmetro e retorne o perímetro do quadrado. 
# No programa principal, solicite o lado e exiba o resultado.

def calcular_perimetro(lado: int):
    calculo = lado * 4
    return calculo

lado = int(input('Digite um lado do quadrado: '))

print(calcular_perimetro(lado))