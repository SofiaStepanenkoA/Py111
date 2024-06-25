from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    car_list = [[0 for _ in range(m)] for _ in range(n)]
    car_list[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue

            paths_from_top = car_list[i - 1][j] if i > 0 else 0
            paths_from_left = car_list[i][j - 1] if j > 0 else 0
            paths_from_diagonal = car_list[i - 1][j - 1] if i > 0 and j > 0 else 0

            car_list[i][j] = paths_from_top + paths_from_left + paths_from_diagonal

    return car_list


if __name__ == '__main__':
    paths = car_paths(4, 2)
    for el in paths:
        print(el)
    print(paths[-1][-1]) #7
