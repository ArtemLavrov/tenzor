import math


#1 задание
print("Введите два числа:")
a, b = float(input()), float(input())
sum = a + b
mult = a * b
division = a / b
stepen = a**b
division_2 = a % b
division_3 = a // b
print(sum, mult, division, division_2, division_3, stepen)

#2 задание
print("Введите ваше имя")
name = input()
print("Здравствуйте " + name +"!")

#3
print("Введите текст") 
print("Последние две буквы в обратном порядке:", input()[-1:-3:-1])


#4
print("Введите радиус круга:")
try:
    print("square circle:", (float(input())**2) * math.pi)

except Exception:
    print("нельзя вводить буквы! Можно воодить только целые числа и дробные")
