num = 234
soma = 0
while num > 0:
    dig = num % 10
    if dig % 2==0:
        soma += dig * 10
    num = num // 10

print(soma)
