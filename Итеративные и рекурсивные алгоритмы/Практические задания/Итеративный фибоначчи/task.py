def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    ...  # TODO написать итеративный алгоритм чисел Фибоначчи
    if not isinstance(n,int):
        raise TypeError
    if n<0:
        raise ValueError
    fib0, fib1 = 0,1
    if n==0:
        return fib0
    if n==1:
        return fib1
    for _ in range (2,n+1):
        fib0, fib1 = fib1, fib0+fib1
    return fib1
