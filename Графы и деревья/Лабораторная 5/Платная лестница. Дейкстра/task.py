from typing import Union

import networkx as nx

def build_graph(graph, stairway):
    node_list=[]
    for step in range(len(stairway)):
        node_list.append(tuple([step, step+1, stairway[step]]))
        if step<9:
            node_list.append(tuple([step, step+2, stairway[step+1]]))
        graph.add_weighted_edges_from(node_list)
        # print(node_list)
    return graph
def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    result = nx.dijkstra_predecessor_and_distance(graph,0)
    for node in graph:
        if node not in result[1]:
            result[1][node] = float('inf')
    list_elem=list(result[1])
    last_elem=list_elem[-1]
    return result[1][last_elem]

if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    graph=nx.DiGraph()
    stairway_graph = build_graph(graph,stairway)  # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    print((stairway_path(stairway_graph)))  # 72
