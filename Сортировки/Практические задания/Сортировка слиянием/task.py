from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализуйте сортировку слиянием
    if len(container)>1:
        mid_ind = len(container)//2
        left_container = sort(container[:mid_ind])
        right_container = sort(container[mid_ind:])
        merge_container=[None]*len(container)
        left_index,right_index, merge_index=0,0,0
        while left_index<len(left_container) and right_index<len(right_container):
            if left_container[left_index]<=right_container[right_index]:
                merge_container[merge_index]=left_container[left_index]
                left_index+=1
            else:
                merge_container[merge_index]=right_container[right_index]
                right_index+=1
            merge_index+=1
        while left_index<len(left_container):
            merge_container[merge_index] = left_container[left_index]
            left_index += 1
            merge_index+=1
        while right_index<len(right_container):
            merge_container[merge_index]=right_container[right_index]
            right_index+=1
            merge_index+=1
        for i in range(len(container)):
            container[i]=merge_container[i]
    return container


