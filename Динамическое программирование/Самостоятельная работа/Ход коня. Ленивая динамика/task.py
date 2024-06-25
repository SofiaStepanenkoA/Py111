from functools import lru_cache
from typing import Tuple

def calculate_paths(shape: Tuple[int, int]) -> int:
    """
    Дано поле с размером N * M посчитать количество маршрутов коня из верхнего левого угла в нижний правый угол.

    :param shape: размер доски в виде кортежа (N, M)
    :return: количество маршрутов согласно заданным условиям
    """
    n, m = shape


    def horse_step(i, j):
        if i == 0 and j == 0:
            return 1
        if i < 0 or i >= n:
            return 0
        if j < 0 or j >= m:
            return 0

        return sum([horse_step(i-2,j+1),horse_step(i-2,j-1),horse_step(i-1,j-2),horse_step(i+1,j-2)])
    return horse_step(n-1,m-1)
if __name__ == '__main__':
    print(calculate_paths((4, 4)))  # 2
    print(calculate_paths((7, 15)))  #  13309
