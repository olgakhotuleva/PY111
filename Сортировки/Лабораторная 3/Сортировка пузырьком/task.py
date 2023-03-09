from typing import Sequence
import random


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    n = len(container)
    #swap = True
    for i in range(n):
        # if not swap:
        #     break
        for j in range(n-i-1):
            if container[j] > container[j+1]:
                #swap = True
                container[j], container[j+1] = container[j+1], container[j]
            # else:
            #     swap = False
    return container


if __name__ == '__main__':
    source_list = [random.randint(0, 20) for _ in range(10)]
    print(source_list)

    sort(source_list)
    print(source_list)
