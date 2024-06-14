from typing import Sequence

def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return container

    max_val = container[0]
    for num in container:
        if num > max_val:
            max_val = num

    Counting_list = [0] * (max_val + 1)

    for num in container:
        Counting_list[num] += 1

    result_list = []
    for i in range(max_val + 1):
        result_list.extend([i] * Counting_list[i])

    return result_list

if __name__ == '__main__':
    print(sort([2, 2, 2, 3, 5, 5, 6, 8, 9, 9, 9, 10]))
