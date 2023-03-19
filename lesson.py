import math

sum = int(input("Введите сумму депозита ", ))

res = sum

for i in range(12):
     res = res + ((res * 0.1274 * 30)/360)
     if((i+1)%3==0):
     	print("Месяц № ",i+1, ", сумма депозита равна ", math.ceil(res))