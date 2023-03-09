"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        raise ValueError("При поиске минимума в пустой последовательности должна возвращаться ошибка")

    min = arr[0]
    i = 0

    for ind, element in enumerate(arr):
        if element < min:
            min = element
            i = ind
        else:
            continue
    return i
