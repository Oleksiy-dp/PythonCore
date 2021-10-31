# Напишите программу, которая вычисляет сумму всех четных чисел от a до b (включительно). Значения a и b вводятся пользователем. 

a = int(input('input a:'))
b = int(input('input b:'))
summ = 0
a += a%2

while a < b:
    summ += a
    a += 2
 
print(summ)