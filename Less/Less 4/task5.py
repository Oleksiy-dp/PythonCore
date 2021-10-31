# Task 5
# The amount of money is known. Exchange it with 200, 100, 10 banknotes and 1 UAH coin, if possible
# Задание 5
# Сумма денег известна. По возможности обменяйте на банкноты 200, 100, 10 и монету 1 грн.
sum = int(input('input sum money: '))
b200 = sum % 200
b100 = sum % 100
b10 = sum % 10
money = 0


if b200 > 0:
    m200 = sum // 200

elif b100 == 0:
    m100 = sum - m200 * 200

elif b10 == 0:
    m10 = m100 - m100*100

elif sum < 10:
    print('Количество купюр номиналом 1 UAH - ', int(sum), ' шт.')
else:
    money = sum//200, '200 UAH', (sum%200)//100, '100 UAH', ((sum%200)%100)//10, '10 UAH', ((sum%200)%100)%10, '1 UAH'
print('Вам положено ', money)
