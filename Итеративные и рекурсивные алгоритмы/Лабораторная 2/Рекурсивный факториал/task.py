def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n == 0:
        return 1
    if not isinstance(n, int):
        raise TypeError("Факториал вычисляется из не целого числа")

    if n < 0:
        raise ValueError("Факториал считается от отрицательного числа")

    return n * factorial_recursive(n - 1)


if __name__ == '__main__':
    print(factorial_recursive(4))
