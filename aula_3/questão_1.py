#Escreva um código em Python que utilize a estrutura de controle ‘if-elif-else' para verificar se um número inteiro dado é
#  par ou ímpar. Se o número for par, armazene-o em uma variável chamada 'pares' e se for ímpar, armazene-o em uma 
# variável chamada 'impares'. Utilize uma única linha de código dentro do bloco 'if' e outra dentro do bloco 'else’.
#OBS: considere zero como neutro (nem par, nem ímpar).




N = int(input("digite um número:"))

pares = 0
impares = 0

N = N%2 == 0


if N % 2 == 0:
    pares = N

elif N % 2 != 0:
    impares = N