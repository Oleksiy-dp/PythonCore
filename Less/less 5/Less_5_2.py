a = int(input('input a:'))
b = int(input('input b:'))
sum = 0
if a%2 == 0:
    a + 1
for i in range(a,b+1,2):
    if i%3 == 0:
        continue
    sum += i
print(sum)
