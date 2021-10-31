#https://all-python.ru/osnovy/chisla.html

# integer - int- целые числа
# float -float - числа с запятой
# String - str - строки
# boolean - bool- булевы выражения 1 or 0,  True or False
# None - # Null
# bin - бинарный
# complex - комплексные = 2 + 4J  - на выходе будет int
#  int / int деление дает Float
# (a // b) деление без остатка - целочисленное деление
# (a ** b) возведение в степень . Степень возводится справа на лево.
# round(10/3) деление с округлениеv - round - округление
# print(d % a) - % -  остаток от деления
# round(10/3, 5) округление до 5-ти знаков
# abs(a)  -модлуль - изменение отрицательного в положительное число
# a += 1 - изменение переменной на 1
# Match,pow(100) - Match математические операции -возведение в степень, корень, логарифмы и т.д

from typing import Match


a = 4
b = 2.34
c = '47385487'
e = True
d = 2
t = True
f = False
n = None # Null 
temp = 14
result = "Holodno" if temp < 10 else "Teplo"

dd = 0b110101 # число в двоичной системе
o = 0o342 # число в восьмеричной системе
x = 0x1FE9 # число в шестнадцатеричной систем

i = int(67.23) # вещественное число усекается до целого
f = float('1304') # строка становится вещественным числом
co = complex(2, 6) # формируется комплексное число
bin = bin(42) # перевод числа в двоичную систему
oct = oct(993) # перевод числа в восьмеричную систему
hex = hex(4152) # перевод числа в шестнадцатеричную систему

print(type(a))
print(type(b))
print(type(c))
print(type(e))

print("dd = " + str(dd))
print("o = " + str(o))
print("x = " + str(x))

print("i = " + str(i))
print("f = " + str(f))
print("co = " + str(co))
print("bin= " + str(bin))
print("oct = " + str(oct))
print("hex = " + str(hex))

print('%')
print(d % a)

print('**')
print(d ** a)

#print(Match,pow(100))

print(a <= b)
print(a >= b)
print(a == b)
print(a != b)

print('Bool')
print ((False or True) and (False and True))
print ((not False and True) and (t or f))
print(None and True)

print('Сравнение')
if temp < 10:
    print("Холодно")
elif 10 <= temp < 28:
    if 10 <= temp < 15:
        print("Holodno, normalno") 
    else: 
        print("very hot, no norm")
else:
    print("Hot")


print('Тернарный оператор')
print(result)

if "":  #если пустой масив данных, пустая строка, то значение равно False и прнит не будет отображаться
    print("Hello")
