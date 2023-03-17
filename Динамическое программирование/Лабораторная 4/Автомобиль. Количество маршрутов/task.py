from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    # TODO решить задачу с помощью динамического программирования

    if not isinstance(n, int):
        raise TypeError()
    if not isinstance(m, int):
        raise TypeError()

    if n < 0 or m < 0:
        raise ValueError()

    if n == m == 0:
        return [[0]]

    table_sum = [[0] * n for _ in range(m)]

    # table_sum[0][0] = 0
    # table_sum[0][1] = 1
    # table_sum[1][0] = 1

    for i in range(0, len(table_sum[0])):
        table_sum[0][i] = 1

    for j in range(0, len(table_sum)):
        table_sum[j][0] = 1

    for i in range(1, len(table_sum)):
        for j in range(1, len(table_sum[0])):
            table_sum[i][j] = table_sum[i - 1][j] + table_sum[i - 1][j - 1] + table_sum[i][j - 1]

    return table_sum


if __name__ == '__main__':
    #paths = car_paths(0, 0)
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
    #print(paths)  # 7
