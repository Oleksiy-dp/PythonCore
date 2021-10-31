n = int(input())
c = [100, 20, 10, 5, 1]
summ = 0
index = 0
count = 0
while index < len(c):
    while (summ + c[index]) <= n:
        summ += c[index]
        count += 1
    index += 1
print(count)