from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """
    ...  # TODO реализовать алгоритм быстрой сортировки
    if len(container)>1:
        middle = container[len(container)//2]
        left_container=[]
        right_container=[]
        equal_counter=0
        for elem in container:
            if elem<middle:
                left_container.append(elem)
            elif elem>middle:
                right_container.append(elem)
            else:
                equal_counter+=1
        return sort(left_container)+equal_counter*[middle]+sort(right_container)
    return container
if __name__=='__main__':
    data = [3, 22, 4, 5, 61, 1, 2,2]
    print(sort(container=data))
