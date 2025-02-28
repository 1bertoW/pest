def maior(num1:int,num2:int):
    if num1 > num2:
        maior = num1
    if num2 > num1:
        maior = num2
    if num1 == num2:
        maior = num1
    return maior

print(maior(10,57))