import re


def check_brackets(brackets_row: str) -> bool:  # O(n)
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """

    stack = []
    for el in brackets_row:
        if el == "(":
            stack.append(el)
        elif stack and el == ")":
            stack.pop()
        else:
            stack.append(el)

    if not stack:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_brackets("(())))"))
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
