import random

def Fibonachi(a):
    """Рекурсивная функция возвращающая заданное число фибоначи.
    string-переменная, обязательно число.
    """
    if a < 2:
        return 1
    return (Fibonachi(a - 1) + Fibonachi(a - 2))


def Sum(a, b):
    """функция показывающая сумму переданных в неё элементов.
    Элементов два и они имеют целочисленные числовые значения
    """
    print(a+b)


def Equals (a, b):
    """Функция, выводящая произведение a и b.
    a - число
    b - число
    """
    print(a*b)


def Del(a, b):
    """Функция возвращающая деление a на b
    a и b целые числа
    """
    return a//b