#Провёл рефакторинг согласно PEP 8 и документацию согласно PEP 257. 
 
########################################################################################################################################################################### 
 
#Второе домашнее задание - рефакторинг 


import math 


#1
print("Введите два числа:") 
a, b = float(input()), float(input()) 
sum = a + b 
mult = a*b 
division = a/b 
stepen = a**b 
division_2 = a%b 
division_3 = a//b 
print(sum, mult, 
      division, division_2, 
      division_3, stepen) 
 
 
#2
 
print("Введите ваше имя") 
name = input() 
print("Здравствуйте " + name + "!") 
 
 
#3 
 
print("Введите текст")  
print("Последние две буквы в обратном порядке:", input()[-1:-3:-1]) 
 
 
#4 

print("Введите радиус круга:") 
try: 
    print("square circle:", (float(input())**2)*math.pi) 

except Exception: 
    print("нельзя вводить буквы! Можно воодить только целые числа и дробные") 


# #Третье домашнее задание - рефакторинг 


#1 Написать скрипт для движения персонажа влево, вправо, вверх и вниз по координатам x и y по координатной оси, начальная позиция персонажа (0;0) 

def path(mass): 
    """Функция определяющая направление и шаг куда будет двигаться персонаж: 
    [0]-направление предполоджительно строка. 
    [1]-шаг-расстояние на которое передвинется персонаж, число. 
    """ 
    try: 
        but=input("Введите направление: ").split() 
        if (but[0] == "вверх" and 
            float(but[1]) >= 0): 
            mass[1] += float(but[1]) 
        elif (but[0] == "вниз" and 
              float(but[1]) >= 0): 
            mass[1] -= float(but[1]) 
        elif (but[0] == "влево" and 
              float(but[1]) >= 0): 
            mass[0] -= float(but[1]) 
        elif (but[0] == "вправо" and 
              float(but[1]) >= 0): 
            mass[0] += float(but[1]) 
        else: 
            raise() 
        print(mass) 
    except Exception: 
        print("Вы ввели некоректные данные! Укажите путь верно!")         


mass=[0,0] 
path(mass) 


#2 Предыдущее, но скрипт бесконечный (каждый раз спрашивается куда движение и выводится результат). Обязательно стоп-слово. 

def path_1(mass): 
    """Бесконечная функция определяющая направление и шаг куда будет двигаться персонаж: 
    [0]-направление предполоджительно строка. 
    [1]-шаг-расстояние на которое передвинется персонаж, число. 
    """ 
    try: 
       while(True): 
            but=input("Введите направление: ").split() 
            print(but) 
            if but[0] == "вверх" and float(but[1]) >= 0: 
                mass[1] += float(but[1]) 
            elif but[0] == "вниз" and float(but[1]) >= 0: 
                mass[1] -= float(but[1]) 
            elif but[0] == "влево" and float(but[1]) >= 0: 
                mass[0] -= float(but[1]) 
            elif but[0] == "вправо" and float(but[1]) >= 0: 
                mass[0] += float(but[1]) 
            elif but[0] == "стоп": 
                print("Вы закончили своё путешевствие!") 
                break        
            else : 
                raise() 
            print(mass) 
    except Exception: 
        print("Вы ввели некоректные данные! Укажите путь верно!")  
        path_1(mass) 


mass=[0,0] 
path_1(mass) 


#3 Написать скрипт решения квадратного уравнения 

def Math_Equation(peremen): 
    """Функция, в которой происходит решение квадратного уравнения 
    [0], [1], [2] - переменные, числа. 
    """ 
    discriminant = (pow(peremen[1], 2)) - (4*peremen[0]*peremen[2]) 
    if discriminant > 0: 
        x_1= (-peremen[1] - pow(discriminant,0.5))/(2*peremen[0]) 
        x_2= (-peremen[1] + pow(discriminant,0.5))/(2*peremen[0]) 
        print(x_1, x_2) 
    elif discriminant == 0: 
        x = -peremen[1]/(2*peremen[0]) 
        print(x) 
    elif discriminant < 0: 
        print("Дискриминант меньше 0. Корней нет! ") 


try: 
    peremen = list(map(float,input("введите переменные a, b, c : ").split())) 
    if peremen[0] == 0.0: 
        print("Это линейное уравнение") 
    Math_Equation(peremen) 
except Exception: 
    print("Введите корректные даныне") 


#4 C обработкой отрицательного дискриминанта (с комплексными числами), со случаем, если коэффициенты являются комплексными числами. 

def Math_Equation_1(a, b, c): 
    """Функция, в которой происходит решение квадратного уравнения с обработкой отрицательного дискриминанта, со случаем если коэфиценты являются комплексными числами 
    [0], [1], [2] - переменные, числа или комплексные числа. 
    """ 
    discriminant = complex((pow(b, 2)) - (4*a*c)) 
    if discriminant != complex(0): 
        x_1 = (-b - pow(discriminant,0.5))/(2*a) 
        x_1 = complex(round(x_1.real,5),round(x_1.imag,5)) 
        x_2 = (-b + pow(discriminant,0.5))/(2*a) 
        x_2 = complex(round(x_2.real,5),round(x_2.imag,5)) 
        if x_1.imag == 0: 
            x_1=x_1.real 
        if x_2.imag == 0: 
            x_2 = x_2.real 
        print(x_1, x_2) 
    if discriminant == 0: 
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
    Math_Equation_1(a, b, c) 


# #Четвертое домашнее задание - рефакторинг 


import random 


#1 Реализовать сортировку списка методом пузырька 

def Bubble(array): 
    """Функция сортировки пузырьком. 
    array - вводимые перменные, числа. 
    """ 
    n=int(input("Введите размерность массива: ")) 
    while(True): 
        request = input("Вы хотите заполнить список с повторяющимися числами?(Y/N): ") 
        if request=="Y": 
            string = input("Введите границы числовых значений, которые хотите видеть в вашем массиве: ").split() 
            a=int(string[0]) 
            b=int(string[1]) 
            for i in range(n): 
                array.append(random.randint(a, b)) 
            print(array) 
            Buble_sort(array) 
            break 
        elif request == "N": 
            array = list(range(0,n)) 
            random.shuffle(array) 
            print(array) 
            Buble_sort(array) 
            print(array) 
            break 
        else: 
            continue 


def Buble_sort(array): 
    """Функция, в которой непосредственно и происходит сортировка. 
    Переменные являются числами. 
    """ 
    a = len(array) 
    for i in range(a-1): 
        for j in range(a-i-1): 
            if array[j]>array[j+1]: 
                array[j],array[j+1]=array[j+1],array[j] 
    print("Список отсортирован") 


array=[] 
Bubble(array) 


# 2 Создать словарь цветов, в котором ключ - название или кодировка цвета; значение - кортеж из rgb этого цвета 

dictionary = { 
    'green': (8, 255, 78), 'red': (255, 8, 8), 
    'blue': (8, 197, 255), 'yellow': (234, 255, 8), 
    'purple' : (251, 8, 255) 
}  
print("Значение RGB этого цвета:", dictionary.get('blue')) 


#3 Заполнить два случайных набора чисел. Вывести оба набора. Указать какие элементы: 
    # входят одновременно в оба; 
    # входят только в первое, но не входят во второе; 
    # входят только во второе, но не входят в первое; 
    # входят в первое или во второе, но не в оба из них одновременно. 

string = input("Введите размерности списков: ").split() 
spisok_1 = {i**2 for i in range(int(string[0]))} 
spisok_2 = {i**2 for i in range(int(string[1]))} 
print(spisok_1, spisok_2) 
print("1) Элементы, которые входят одновременно в оба:", spisok_1 & spisok_2) 
print("2) Элементы, которые входят только в первое, но не входят во второе:", spisok_1.difference(spisok_2)) 
print("3) Элементы, которые входят только во второе, но не входят во первое:", spisok_2.difference(spisok_1)) 
print("4) Элементы, которые входят в первое или во второе, но не в оба из них одновременно:", spisok_1.symmetric_difference(spisok_2)) 


#4 Создать игровой инвентарь. Должна быть возможность добавлять в него предметы и удалять предметы из него. 
#  Инвентарь должен быть ограничен по весу, каждый предмет имеет свой вес. Вывод предметов должен быть с названием предмета и его весом. 

count = 0 
inventory = dict() 
size = float(input("Введите максимальное количество киллограм которое вы сможете нести: " )) 
while count < size + 0.1: 
    item = input("Название предмета и его вес: ").split() 
    if item[0].isalpha() and item[1].isdigit(): 
        if float(item[1]) <= size: 
            if count+float(item[1]) <= size: 
                inventory.update({item[0] : float(item[1])}) 
                count += float(item[1])         
                print(inventory) 
                print(count) 
                while True: 
                    questions = input("Хотите что нибудь удалить из инвентаря (Y/N): ")                 
                    if questions == "Y": 
                        dell = input("Какой предмет хотите удалить: ") 
                        inventory.pop(dell) 
                        print(inventory) 
                    elif questions == "N":  
                        print("Продолжим искать полезные предметы!") 
                        break              
                    elif questions == "стоп": 
                        break 
                    else:  
                        print("Я вас не понимаю... Ответьте: (Y/N)")                       
                        continue 
                if questions == "стоп": 
                    break 
            else: 
                while True: 
                    questions=input("Инвернтарь переполнен. Хотите удалить какой то предмет? : ") 
                    if questions == "Y": 
                        dell=input("Какой предмет хотите удалить: ") 
                        if dell in inventory: 
                            inventory.pop(dell) 
                            print(inventory) 
                            break 
                    elif questions == "N": 
                        print("Вы не можете подобрать данный предмет, так как ваш инвернтарь переполнен") 
                        break 
                    else: 
                        print("Введите ответ корректно - (Y/N):") 
                        break 
        else: 
            print("Вы не сможете это поднять!") 
            continue 
    else: 
        print("Странный предмет, попробуйте взять что то другое!") 
        continue 


# # Пятое домашнее задание - рефакторинг 


#1Написать функцию, принимающую строку-пароль. Функция должна проверить подходит ли этот пароль условиям и вернуть True - если подходит; False - если не подходит. Условия: 
def check_password(string): 
    """Функция принимающая строку пароль и возвращающая значение True или False. 
    string - строка или целые числа. 
    """ 
    count = 0 
    if len(string) >= 6: 
        count += 1 
    else: 
        return False 
    if string.isdigit(): 
            return False 
    else: 
        count += 1 
    if string.isalpha(): 
            return False 
    else: 
        for i in range(len(string)): 
            if string[i].isdigit(): 
                break 
        count += 1 
    if "password" not in string.lower(): 
        count += 1 
    if count == 4: 
        return True 
    else: 
        return False 


string=input("Введите ваш пароль: ") 
print(check_password(string)) 



# #2 Написать функцию, принимающую сколько угодно параметров  

def NFunc (*nargs): 
    """Функция, принимающую сколько угодно параметров. 
    nargs-любой параметр. 
    """ 
    sum = 0 
    for i in range(len(nargs[0])): 
        sum += int(nargs[0][i]) 
    print(sum) 


while True: 
    string = input("Введите числа которые хотите сложить. Можете ввести слово стоп чтобы прекратить действие программы: ").split() 
    try: 
        if string[0] == "стоп": 
            break 
        NFunc(*string) 
    except: 
        print("Вводите данные коректно") 


#3 Написать функцию, которая возвращает заданное число Фибоначчи (рекурсия). 

def Fibonachi(string): 
    """Рекурсивная функция возвращающая заданное число фибоначи. 
    string-переменная, обязательно число. 
    """ 
    if string < 2: 
        return 1 
    return (Fibonachi(string - 1) + Fibonachi(string - 2)) 


while True: 
    try: 
        string = int(input("введите интересующие вас число фибоначи: ")) 
        if string == "стоп": 
            break 
        print("Вот это число: ",Fibonachi(string)) 
        break 
    except: 
        print("Введите данные коректно!") 


# #Шестое домашнее задание - рефакторинг 


# #1 Написать функцию преобразующую список строк, в список байт кодов. Написать обратную функцию. 

def string_to_bytes(string):
    """Функция перевода элементов списка строк в список байтов. 
    string-строка.
    """ 
    string_bytes = list()
    for i in range(len(string)):
        print("Элемент {a} имеет тип {b} ".format(a = string[i], b = type(string[i])))
        string_bytes.append(string[i].encode("UTF-8")) 
        print("Элемент {a}, после преобразования, имеет тип данных {b} ".format(a = string_bytes[i], b = type(string_bytes[i]))) 
        for j in string_bytes[i]: 
            print(j, end = '') 
        print() 
    bytes_to_string(string_bytes)


def bytes_to_string(string_bytes): 
    """Функция перевода списка байтов в список строк 
    string_bytes - списко байтов 
    """ 
    bytes_string = list() 
    for i in range(len(string_bytes)): 
        bytes_string.append(string_bytes[i].decode()) 
    for i in range(len(bytes_string)): 
        print("Элемент {a} после обратного преобразования имеет тип {b}".format(a = bytes_string[i], b = type(bytes_string[i]))) 


string = input("Введите слова которые хотите видеть в списке через пробел: ").split() 
string_to_bytes(string) 
 
#2 Формула молекулы спирта - C2H5(OH). Из неё видно, что молекула состоит из двух атомов углерода (С), 6 атомов водорода (Н) и одного атома кислорода (О). 
#  В Input.txt содержится 3 натуральных числа: C, H, O – количество атомов углерода, водорода и кислорода соответственно. 
#  В файл Output.txt вывести максимально возможное число молекул спирта, которые могут получиться из атомов, представленных во входных данных. 


def count_spirt(string): 
    """Функция подсчитывающая количество молеул спирта. 
    string - принимает целые числа 
    """ 
    values = list() 
    if (int(string[0]) >= 2 
            and int(string[1]) >= 6 
            and int(string[2]) >= 1): 
        C = int(string[0])//2 
        values.append(C) 
        H = int(string[1])//6 
        values.append(H) 
        O = int(string[2])//1 
        values.append(O) 
        values.sort() 
    with open('C:/Users/Artem/Desktop/Tenzor/tenzor/six_dz/output.txt','w', encoding = "UTF-8") as w: 
        w.write("Максимально возможное число молекул спирта: {a}".format(a = values[0])) 


with open('C:/Users/Artem/Desktop/Tenzor/Tenzor/six_dz/input.txt', 'r', encoding = "UTF-8") as re: 
    string = re.read().split() 
    count_spirt(string) 


#3 XOR шифрование/расшифрование. На входе файл с текстом и ключ шифрования (строка), на выходе преобразованное (зашифрованное/расшифрованное) сообщение в файле. 

def XOR_encription_discription(text,key): 
    """Функция шифравания текста по ключу. 
    text - строка, key - числовое значение. 
    """ 
    encript_str = str() 
    for i in range(len(text)): 
        encript_str += chr(ord(text[i])^key) 
    return encript_str 


with open('tenzor\six_dz\input_1.txt','r',encoding = "UTF-8")as r: 
    string = r.readline() 
    key = int(r.readline())     
    encoding_str = XOR_encription_discription(string,key) 

with open('tenzor\six_dz\output_1.txt','w',encoding = "UTF-8") as w: 
    w.write("Зашифрованная строка: {a}".format(a = encoding_str)) 
    w.write("\n" 
            + "Расшифрованная строка: "  
            + XOR_encription_discription(encoding_str,key)) 
 
####################################################################################################################################################################### 