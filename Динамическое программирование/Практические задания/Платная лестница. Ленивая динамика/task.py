from typing import Union, Sequence
from functools import lru_cache


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO реализовать ленивую динамику
    def stairway_lazy(stair):
        if stair==0 or stair ==1:
            return stairway[stair]
        return stairway[stair]+min(stairway_lazy(stair-1),stairway_lazy(stair-2))
    return stairway_lazy(len(stairway)-1)

if __name__ == '__main__':
    print(stairway_path((1, 3, 1, 5)))  # 7
