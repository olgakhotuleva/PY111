"""
My little Queue
"""
import pprint
from typing import Any
import random


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        """
        self._queue = [] # TODO инициализировать список

    def enqueue(self, elem: Any) -> None: #O(1)
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self._queue.append(elem)

    def dequeue(self) -> Any: # O(1)
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        for ind, elem in enumerate(self._queue):
            return self._queue.pop(ind)

        raise IndexError("Пустая очередь")

    def peek(self, ind: int = 0) -> Any: #O(1)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Индекс должен быть целочисленным")

        if not 0 <= ind <= len(self._queue):
            raise IndexError("Индек вне границ очереди")
        return self._queue[ind]

    def clear(self) -> None: #O(1)
        """ Очистка очереди. """
        self._queue.clear()

    def __len__(self): #O(1)
        """ Количество элементов в очереди. """
        return len(self._queue)

    def __str__(self):
        pprint.pprint(self._queue) # O(N)
        return ""


if __name__ == '__main__':
    pq = Queue()
    for i in range(10):
        pq.enqueue(random.randint(1, 20))
    pq.enqueue(333)
    print(pq)
    print(pq.dequeue())
