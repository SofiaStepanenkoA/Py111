from typing import List


def rocket_coasts(table: List[List[int]]) -> List[List[int]]:
    """

    Просчитать минимальные стоимости маршрутов до каждой клетки с учетом возможных перемещений.


    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё
    :return: Таблицу стоимостей перемещения по клеткам
    """
    ...  # TODO рассчитать таблицу стоимостей перемещений
    if not isinstance(table,list):
        raise(TypeError)
    result_table=table.copy()
    for i in range(1,len(result_table[0])):
        result_table[0][i]+=result_table[0][i-1]
    for i in range(1,len(result_table)):
        result_table[i][0]+=result_table[i-1][0]
    for i in range(1,len(result_table)):
        for j in range(1,len(result_table[0])):
            result_table[i][j]+=min(result_table[i-1][j],result_table[i][j-1])
    return result_table

if __name__ == '__main__':
    coasts_ceil = [
        [2, 7, 9, 3],
        [12, 4, 1, 9],
        [1, 5, 2, 5]
    ]
    total_coasts = rocket_coasts(coasts_ceil)
    for el in total_coasts:
        print(el)
    print(total_coasts[-1][-1])  # 21
