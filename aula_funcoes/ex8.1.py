# Implemente uma função chamada quadrado que receba um número como parâmetro e retorne o valor do número elevado ao quadrado. Solicite ao usuário um 
# número e exiba o resultado retornado.

def quadrado(numero: int):
    valor = numero ** 2
    return valor

numero = int(input('Digite um número: '))

print(quadrado(numero))