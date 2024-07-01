from typing import Hashable, List
from collections import deque

import networkx as nx
from matplotlib import pyplot as plt

def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в ширину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    ...  # TODO реализовать обход в ширину
    qeue_=[start_node] #очередь веошин для посещения
    visited=set() #множество посещенных вершин
    result_list=[] #порядок посед=щения вершин
    visited.add(start_node)
    while qeue_:
        visited_node = qeue_.pop(0)
        result_list.append(visited_node)
        for elem in g[visited_node]:
            if elem not in visited:
                qeue_.append(elem)
                visited.add(elem)
    return result_list


if __name__ == '__main__':
    # TODO записать граф с помощью модуля networkx и прверить обход в ширину
    graph = nx.Graph()
    graph.add_nodes_from('ABFGCHIJED')
    graph.add_edges_from([('A','B'),
                          ('A','F'),
                          ('B','G'),
                          ('F','G'),
                          ('G','C'),
                          ('G','H'),
                          ('C','H'),
                          ('H','I'),
                          ('G','I'),
                          ('H','J'),
                          ('H','E'),
                          ('H','D'),
                          ('E','D')])
    # nx.draw_spring(graph,node_color='purple',node_size=1000,with_labels=True)
    # plt.show()
    print(bfs(graph,'A'))