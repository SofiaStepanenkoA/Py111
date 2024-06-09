from typing import Union
from itertools import count
from math import factorial
import math

DELTA = 0.000001


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    ...  # TODO вычислить sin(x) с помощью разложения сумму бесконечного ряда
    sin=x
    iter=0
    sum=sin
    print(sin)
    while abs(sin)>DELTA:
        iter+=1
        sin=((-1)**(iter))*((x)**(2*iter+1))/factorial(2*iter+1)
        sum+=sin
        print(f'sum:{sum}, n={iter},вклад{sin}')
    return sum
# print(sinx(math.pi))
