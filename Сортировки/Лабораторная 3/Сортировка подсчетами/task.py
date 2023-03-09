from typing import Sequence
import random


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return container

    max_el = max(container)
    tmp = [0]*(max_el+1)
    for i in container:
        tmp[i] += 1

    print(tmp)

    k = 0
    for i in range(len(tmp)):
        while tmp[i] > 0:
            container[k] = i
            tmp[i] -= 1
            k += 1

    return container




if __name__ == '__main__':
    source_list = [random.randint(0, 20) for _ in range(10)]
    source_list = [14, 20, 15, 17, 17, 20, 9, 15, 8, 13, 14, 0]
    print(source_list)
    print(len(source_list))

    print(sort(source_list))
