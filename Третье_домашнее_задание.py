#1 Написать скрипт для движения персонажа влево, вправо, вверх и вниз по координатам x и y по координатной оси, начальная позиция персонажа (0;0)

def path(mass):
    try:
        but=input("Введите направление: ").split()
        if but[0] == "вверх" and float(but[1]) >= 0 :
            mass[1] += float(but[1])
        elif but[0] == "вниз" and float(but[1]) >= 0 :
            mass[1] -= float(but[1])
        elif but[0] == "влево" and float(but[1]) >= 0 :
            mass[0] -= float(but[1])
        elif but[0] == "вправо" and float(but[1]) >= 0 :
            mass[0] += float(but[1])
        else :
            raise()
        print(mass)
    except Exception:
        print("Вы ввели некоректные данные! Укажите путь верно!")        

mass=[0,0]
path(mass)

#2 Предыдущее, но скрипт бесконечный (каждый раз спрашивается куда движение и выводится результат). Обязательно стоп-слово.

def path(mass):
    try:
       while(True):
            but=input("Введите направление: ").split()
            print(but)
            if but[0] == "вверх" and float(but[1]) >= 0 :
                mass[1] += float(but[1])
            elif but[0] == "вниз" and float(but[1]) >= 0 :
                mass[1] -= float(but[1])
            elif but[0] == "влево" and float(but[1]) >= 0 :
                mass[0] -= float(but[1])
            elif but[0] == "вправо" and float(but[1]) >= 0 :
                mass[0] += float(but[1])
            elif but[0] == "стоп":
                print("Вы закончили своё путешевствие!")
                break       
            else :
                raise()
            print(mass)
    except Exception:
        print("Вы ввели некоректные данные! Укажите путь верно!") 
        path(mass)

mass=[0,0]
path(mass)

#3 Написать скрипт решения квадратного уравнения

def Math_Equation(peremen):
    discriminant = (pow(peremen[1], 2))-(4*peremen[0]*peremen[2])
    if discriminant>0:
        x_1= (-peremen[1] - pow(discriminant,0.5))/(2*peremen[0])
        x_2= (-peremen[1] + pow(discriminant,0.5))/(2*peremen[0])
        print(x_1, x_2)
    elif discriminant==0:
        x = -peremen[1]/(2*peremen[0])
        print(x)
    elif discriminant < 0:
        print("Дискриминант меньше 0. Корней нет! ")


try:
    peremen = list(map(float,input("введите переменные a, b, c : ").split()))
    if peremen[0]==0.0:
        print("Это линейное уравнение")
    Math_Equation(peremen)
except Exception:
    print("Введите корректные даныне")

#4 C обработкой отрицательного дискриминанта (с комплексными числами), со случаем, если коэффициенты являются комплексными числами.

def Math_Equation(a, b, c):
    discriminant = complex((pow(b, 2))-(4*a*c))
    if discriminant!=complex(0):
        x_1= (-b - pow(discriminant,0.5))/(2*a)
        x_1 = complex(round(x_1.real,5),round(x_1.imag,5))
        x_2= (-b + pow(discriminant,0.5))/(2*a)
        x_2 = complex(round(x_2.real,5),round(x_2.imag,5))
        if x_1.imag == 0:
            x_1=x_1.real
        if x_2.imag == 0:
            x_2=x_2.real
        print(x_1, x_2)
    if discriminant==0:
        x = -b/(2*a)
        x = complex(round(x.real,5),round(x.imag,5))
        print(x)
        

peremen = input("введите переменные a, b, c : ").split()
a = complex(peremen[0])
b = complex(peremen[1])
c = complex(peremen[2])
if a == 0:
    print("Это линейное уравнение")
    exit 
else:
    Math_Equation(a, b, c)


    
