from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы

    target = graph.number_of_nodes() - 1
    return nx.shortest_path_length(graph, source=0, target=target, weight='weight')


def func(stairway: set):
    count_stairs = len(stairway)
    list_ = []
    for i in range(0, count_stairs - 1):
        list_.append((i, i + 1, stairway[i]))
        list_.append((i, i + 2, stairway[i + 1]))
    list_.append((count_stairs - 1, count_stairs, stairway[-1]))
    return list_


if __name__ == '__main__':

    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)

    # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней

    stairway_graph = nx.DiGraph()
    stairway_graph.add_weighted_edges_from(func(stairway))
    # stairway_graph.add_weighted_edges_from([
    #     (0, 1, 5),
    #     (0, 2, 11),
    #     (1, 2, 11),
    #     (1, 3, 43),
    #     (2, 3, 43),
    #     (2, 4, 2 ),
    #     (3, 4, 2),
    #     (3, 5, 23),
    # ])

    print(stairway_path(stairway_graph))  # 72
