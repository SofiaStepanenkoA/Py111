from typing import Sequence


def binary_search(
        value: int, seq: Sequence[int],
        left_border: int = 0, right_border: int = None
) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск
    :param left_border: Левая граница массива, нужна для рекурсивного алгоритма
    :param right_border: Правая граница массива, нужна для рекурсивного алгоритма

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    ...  # TODO реализовать алгоритм бинарного поиска
    if not right_border:
        right_border=len(seq)-1
    if right_border<left_border:
        raise ValueError
    mid = (right_border+left_border)//2
    if value<seq[mid]:
        return binary_search(value,seq,left_border,mid-1)
    elif value>seq[mid]:
        return binary_search(value, seq, mid+1, right_border)
    else:
        while seq[mid-1]==value and mid > left_border:
            mid-=1
        return mid

