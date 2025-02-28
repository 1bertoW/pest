#Crie uma função chamada duplicar_metade que receba uma string e retorne a primeira metade
#a string duplicada.
#

def duplicar_metade(string):
    metade = len(string)//2
    return string[:metade]* 2

print(duplicar_metade("progamar"))



