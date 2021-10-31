name = "Мой курс"
s = "Python быстрый старт"
s1 = 'Python'
s2 = "Python 'быстрый' старт"
s3 = "Python \"быстрый\" старт"
s4 = "Python \nбыстрый\t старт"  # - \n перенос строки; \t - табуляция
s5 = "Python \nбыстрый\n\t старт"  # - \n перенос строки; \t - табуляция
s6 = "Python \nбыстрый\n\t\r старт"  # - \r - возврат каретки
s7 = """
Самый лучший день
приходил вчера
"""
s8 = '''
Самый лучший день
    приходил вчера
 ночью как плед
'''
s9 = r"Python \nбыстрый\n\t\r старт"  # -префикс r перед строкой исключает все спец символы (\n\t\r) и определяет все как строку
s10 = "Hello, %s" % name # %s - указывает на тип данных строка
s11 = "Hello, %s %d" % (s, 10) # %s - тип данных строка, %d - число
s12 = "Hello, %s %f" % (s, 10) # %s - тип данных строка, %f - число c pfgznjq
s13 = "Hello, {} {}".format(name, 33)
s14 = "Hello, {greet_name} {number}".format(greet_name=name, number=48)
s15 = f"Hello, {name}" 


print(s)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
print(s8)

print(name + s)
print(name + " " + s)
print(s9)

print(name[0]) # обращение к первому символу имени. начинается с нуля
print(name[-1]) # обращение к первому символу с конца
print(name[0:6]) # масив данных 7 символов
print(len(name)) # len - длинва строки
print("Мой ку" in name) # проверка на вхождение, присутсвуют ли символы "Мой ку" в строке - True,False

print(s10)
print(s11)
print(s12)
print(s13)
print(s14)
print(s15)

