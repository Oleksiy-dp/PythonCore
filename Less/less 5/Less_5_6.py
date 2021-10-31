# Write a program that calculates the sum of all odd numbers between a and b (inclusive). The values ​​of a and b are entered by the user.
# Напишите программу, которая вычисляет сумму всех нечетных чисел от a до b (включительно). Значения a и b вводятся пользователем.

a = int(input('inp A:'))
b = int(input('inp B:'))
sum = 0

if a % 2 == 0:
    a += 1

for i in range(a, b+1, 2):
    sum += i
    print(i)
print(sum)