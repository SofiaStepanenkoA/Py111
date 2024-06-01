def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    stack = []
    if not isinstance(brackets_row,str):  # TODO реализовать проверку скобочной группы
        raise ValueError
    if not brackets_row:
        return True
    for i in brackets_row:
        if (i =='('):
            stack.append(i)
        if (i==')') and (stack):
            stack.pop()
        elif (i==')') and not stack:
            return False
    if len(stack)!=0:
        return False
    else:
        return True



if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
