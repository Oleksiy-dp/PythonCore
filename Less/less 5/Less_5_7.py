# найти сумму всех не парных чисел  от a до b не учитывая тех кто делится на 3.

a = int(input('inp A:'))
b = int(input('inp B:'))


sum = 0

if (a % 2 == 0):
    a += 1
    
for i in range(a, b+1, 2):
    if (i % 3 == 0):
        continue
    sum += i
    print(i)
print(sum)