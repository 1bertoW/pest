#Crie uma função chamada intervalo que receba uma string e dois índices inteiros. A função
#deve retornar a substring que está entre esses dois índices, incluindo o caractere no primeiro
#índice, mas excluindo o do último.

def intervalo(string:str,ind1:int,ind2:2):
    return string[ind1:ind2]
   

sub = intervalo("python",1,4)
print(sub)
