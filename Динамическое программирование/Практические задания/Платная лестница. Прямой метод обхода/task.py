from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO реализовать прямой метод расчета
    if not stairway:
        raise(ValueError)

    count_stairs=len(stairway)
    if count_stairs==1:
        return stairway[0]
    if count_stairs==2:
        return stairway[1]
    result_list = [stairway[0],stairway[1]]

    for i in range(2,len(stairway)):
        result_list.append(min(result_list[i-1],result_list[i-2])+stairway[i])
    return result_list[-1]


if __name__ == '__main__':
    print(stairway_path([1, 3, 1, 5]))  # 7
