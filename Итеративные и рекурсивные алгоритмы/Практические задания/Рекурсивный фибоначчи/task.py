def fib_recursive(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя рекурсивный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    ...  # TODO реализовать рекурсивный алгоритм
    if not isinstance(n,int):
        raise TypeError
    if n<0:
        raise ValueError
    fib0, fib1 = 0,1
    if n==0:
        return fib0
    if n==1:
        return fib1
    return fib_recursive(n-1)+fib_recursive(n-2)