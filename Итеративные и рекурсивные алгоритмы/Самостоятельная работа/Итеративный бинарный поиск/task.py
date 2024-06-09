from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    ...  # TODO реализовать итеративный алгоритм бинарного поиска
    ...  # TODO реализовать алгоритм бинарного поиска
    if not seq:
        raise ValueError("sequence is empty")
    right_border = len(seq)-1
    left_border=0
    index=-1
    if left_border==right_border and seq[0]!=value:
        raise ValueError("single element sequence is not equal to value")
    while left_border<right_border:

        mid = (right_border + left_border) // 2
        # print(f'left border:{left_border}, right border:{right_border}, mid:{mid}')
        # print(seq[left_border:right_border])
        if value < seq[mid]:
            right_border=mid-1
        elif value > seq[mid]:
            left_border=mid+1
        elif value==seq[mid] and seq[mid]==seq[mid-1]:
            index=mid-1
            mid=mid-1
            right_border-=1
        else:
            return mid

    if left_border==right_border and value==seq[left_border]:
        return left_border
    elif index==-1:
        # print(mid)
        # print(left_border)
        # print(right_border)
        raise ValueError("element not found")
    return index
# print (binary_search(1,[1,22,34,56]))