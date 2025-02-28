def maior(num1:float,num2:float):
    if num1 > num2:
        print(f"o numero {num1} é maior que {num2}")
    if num2 > num1:
        print(f"o numero {num2} é maior que {num1}")
    if num1 == num2:
        print("os numeros são iguais")
    
maior(10,10)