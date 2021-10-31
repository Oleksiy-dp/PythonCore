# Задача: распечатать каждый символ в строке.
# Task: Print each character in the string.

userName = input('Enter name: ')
i = 0
while i < len(userName):
    letter = userName[i]
    print(letter)
    i += 1