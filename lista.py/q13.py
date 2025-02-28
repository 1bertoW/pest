#Escreva uma função chamada trocar_metades que troque a primeira metade de uma string
#ela segunda metade e retorne a nova string.

def trocar_meta(a):
    meio = len(a) // 2
    return a[meio:] + a[:meio]
print(trocar_meta("gabo"))