
N = int(input("corno digite um numero:"))
numero_investidor = 0

while N > 0:
    dig = N %10    
    numero_investidor =  dig + (numero_investidor*10)
    N = N//10
print(numero_investidor)


