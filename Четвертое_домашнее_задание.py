import random


# #1 Реализовать сортировку списка методом пузырька
def Bubble(array):    
    n=int(input("Введите размерность массива: "))    
    while(True):        
        request = input("Вы хотите заполнить список с повторяющимися числами?(Y/N): ")
        if request=="Y" :
            string = input("Введите границы числовых значений, которые хотите видеть в вашем массиве: ").split()
            a=int(string[0])
            b=int(string[1])                
            for i in range(n):
                array.append(random.randint(a, b))
            print(array)
            Buble_sort(array)
            break
        elif request == "N" :
            array = list(range(0,n))
            random.shuffle(array)
            print(array)
            Buble_sort(array)
            print(array)
            break
        else:
            continue              
    
    
def Buble_sort(array):
    a = len(array)    
    for i in range(a-1):
        for j in range(a-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    print("Список отсортирован")

array=[]
Bubble(array)


# # 2 Создать словарь цветов, в котором ключ - название или кодировка цвета; значение - кортеж из rgb этого цвета
dictionary = {'green': (8, 255, 78), 'red': (255, 8, 8), 'blue': (8, 197, 255), 'yellow': (234, 255, 8), 'purple' : (251, 8, 255)} 
print("Значение RGB этого цвета:", dictionary.get('blue'))




##3 Заполнить два случайных набора чисел. Вывести оба набора. Указать какие элементы:
    ## входят одновременно в оба;
    ## входят только в первое, но не входят во второе;
    ## входят только во второе, но не входят в первое;
    ## входят в первое или во второе, но не в оба из них одновременно.

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
count=0
inventory=dict()
size = float(input("Введите максимальное количество киллограм которое вы сможете нести: " ))
while count<size+0.1:
    item=input("Название предмета и его вес: ").split()
    if item[0].isalpha() and item[1].isdigit():
        if float(item[1])<=size:
            if count+float(item[1])<=size:
                inventory.update({item[0] : float(item[1])})
                count+=float(item[1])        
                print(inventory)
                print(count)
                while True:
                    questions=input("Хотите что нибудь удалить из инвентаря (Y/N): ")                
                    if questions=="Y":
                        dell=input("Какой предмет хотите удалить: ")
                        inventory.pop(dell)
                        print(inventory)
                    elif questions=="N": 
                        print("Продолжим искать полезные предметы!")
                        break             
                    elif questions=="стоп":
                        break
                    else: 
                        print("Я вас не понимаю... Ответьте: (Y/N)")                      
                        continue
                if questions == "стоп":
                    break
            else:
                while True:
                    questions=input("Инвернтарь переполнен. Хотите удалить какой то предмет? : ")
                    if questions=="Y":                       
                        dell=input("Какой предмет хотите удалить: ")
                        if dell in inventory:
                            inventory.pop(dell)
                            print(inventory)
                            break
                    elif questions=="N":
                        print("Вы не можете подобрать данный предмет, так как ваш инвернтарь переполнен")
                        break
                    else :
                        print("Введите ответ корректно - (Y/N):")
                        break
        else:
            print("Вы не сможете это поднять!")
            continue
    else:
        print("Странный предмет, попробуйте взять что то другое!")
        continue

    
    

