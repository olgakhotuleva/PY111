def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n == 0:
        return 1
    if not isinstance(n, int):
        raise TypeError("Факториал вычисляется из не целого числа")

    if n < 0:
        raise ValueError("Факториал считается от отрицательного числа")

    el = 1
    for i in range(1, n+1):
       el *= i
    return el