# #1Написать функцию, принимающую строку-пароль. Функция должна проверить подходит ли этот пароль условиям и вернуть True - если подходит; False - если не подходит. Условия:
def check_password(string):
    count=0 
    if len(string)>=6: 
        count+=1      
    else:
        return False

    if string.isdigit():
            return False
    else:
        count+=1
    
    if string.isalpha():
            return False
    else:
        for i in range(len(string)):
            
            if string[i].isdigit():
                break                                                      
        count+=1   
          
    if "password" not in string.lower():
        count+=1

    if count==4:
        return True 
    else:
        return False   

string=input("Введите ваш пароль: ")
print(check_password(string))



# #2 Написать функцию, принимающую сколько угодно параметров 

def NFunc (*nargs):
    sum=0
    for i in range(len(nargs[0])):
        sum += int(nargs[0][i]) 
    print(sum)  
    
while True:
    string=input("Введите числа которые хотите сложить. Можете ввести слово стоп чтобы прекратить действие программы: ").split()
    try:
        if string[0]=="стоп":
            break
        NFunc(string)
    except:
        print("Вводите данные коректно")

#3 Написать функцию, которая возвращает заданное число Фибоначчи (рекурсия).

def Fibonachi(string):
    if string < 2:
        return 1
    return (Fibonachi(string-1)+Fibonachi(string-2))

while True:    
    try:
        string=int(input("введите интересующие вас число фибоначи: "))
        if string=="стоп":
            break
        print("Вот это число: ",Fibonachi(string))
        break
    except:
        print("Введите данные коректно!")

    

