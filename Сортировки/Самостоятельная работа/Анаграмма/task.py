def sort(container: str) -> str:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки пузырьком
    sorted_str=list(container)
    print(sorted_str)
    for i in range(len(sorted_str)):
        for j in range(len(sorted_str)):
            if sorted_str[i]<sorted_str[j]:
                sorted_str[i],sorted_str[j]= sorted_str[j], sorted_str[i]
    return sorted_str
def is_anagram(s: str, t: str) -> bool:
    if sort(s)==sort(t):
        return True
    else:
        return False


if __name__=="__main__":
    print(is_anagram("anagram","nagaram"))
