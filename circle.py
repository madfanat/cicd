import math


def area(r):
    '''
    Принимает длину радиуса круга r (float)
    Возвращает приблизительную площадь круга радиуса r (float)
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает длину радиуса круга r (float)
    Возвращает приблизительную длину окружности радиуса r (float)
    '''
    return 2 * math.pi * r

