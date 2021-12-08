#1 Написать функцию преобразующую список строк, в список байт кодов. Написать обратную функцию.
def string_to_bytes(string): 
    string_bytes=list()   
    for i in range(len(string)):
        print("Элемент {a} имеет тип {b} ".format(a=string[i],b=type(string[i])))    
        string_bytes.append(string[i].encode("UTF-8"))
        print("Элемент {a}, после преобразования, имеет тип данных {b} ".format(a=string_bytes[i],b=type(string_bytes[i])))
        for j in string_bytes[i]:            
            print(j, end = '')
        print()
    bytes_to_string(string_bytes)
def bytes_to_string(string_bytes):
    bytes_string=list()
    for i in range(len(string_bytes)):        
        bytes_string.append(string_bytes[i].decode())
    for i in range(len(bytes_string)):
        print("Элемент {a} после обратного преобразования имеет тип {b}".format(a=bytes_string[i],b=type(bytes_string[i])))


string = input("Введите слова которые хотите видеть в списке через пробел: ").split()
string_to_bytes(string)



#2 Формула молекулы спирта - C2H5(OH). Из неё видно, что молекула состоит из двух атомов углерода (С), 6 атомов водорода (Н) и одного атома кислорода (О).
#  В Input.txt содержится 3 натуральных числа: C, H, O – количество атомов углерода, водорода и кислорода соответственно.
#  В файл Output.txt вывести максимально возможное число молекул спирта, которые могут получиться из атомов, представленных во входных данных.

def count_spirt(string):
    values=list()
    if(int(string[0])>=2 and int(string[1])>=6 and int(string[2])>=1):
        C=int(string[0])//2
        values.append(C)
        H=int(string[1])//6
        values.append(H)
        O=int(string[2])//1
        values.append(O)
        values.sort()
    with open('C:/Users/Artem/Desktop/Tenzor/tenzor/six_dz/output.txt','w',encoding="UTF-8") as w:
        w.write("Максимально возможное число молекул спирта: {a}".format(a=values[0]))
    

with open('C:/Users/Artem/Desktop/Tenzor/Tenzor/six_dz/input.txt', 'r',encoding="UTF-8") as re:
    string=re.read().split()
    count_spirt(string)

#3 XOR шифрование/расшифрование. На входе файл с текстом и ключ шифрования (строка), на выходе преобразованное (зашифрованное/расшифрованное) сообщение в файле.

def XOR_encription_discription(text,key):
    encript_str=str()
    for i in range(len(text)):
        encript_str+=chr(ord(text[i])^key)
    return encript_str
    

with open('tenzor\six_dz\input_1.txt','r',encoding="UTF-8")as r:
    string=r.readline()
    key=int(r.readline())    
    encoding_str=XOR_encription_discription(string,key)
with open('tenzor\six_dz\output_1.txt','w',encoding="UTF-8") as w:
    w.write("Зашифрованная строка: {a}".format(a=encoding_str))
    w.write("\n"+ "Расшифрованная строка: " + XOR_encription_discription(encoding_str,key))
    