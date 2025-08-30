import time

def slow_typing(text, speed=0.1):
    for char in text:
        print(char, end='')
        time.sleep(speed)
    print()

def bmi_calc(weight, height):
    bmi = (weight / (height * height) * 10000)
    return round(bmi, 2)
