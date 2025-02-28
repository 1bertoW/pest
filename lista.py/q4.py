#crie função chamada repetir_palavra que receba uma string e um número inteiro n e
#etorne a string repetida n vezes.

def repete_palavra(palavra:str,numero:int):
    return palavra * numero
entrada_palavra = "oi"
entrada_numero = 3
saida = repete_palavra(entrada_palavra,entrada_numero)
print(saida)

