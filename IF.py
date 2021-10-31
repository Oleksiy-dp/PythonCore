temp = int(input('temp: '))

if temp < 10:
    print("Cold")
elif 10 <= temp < 28:
    if 10 <= temp < 15:
        print("Holodno, no norm")
    else:
        print("Very hot, no normalno")
else:
    print("Very hot!")