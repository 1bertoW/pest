num = int(input("digite um numero de 4 digitos:"))

cal = (num%10)
cal2 = (num//10)%10
cal3 = (num//100)%10
cal4 = num//1000%10

cal_final = cal + cal2 + cal3 + cal4

print(f"{cal_final}")