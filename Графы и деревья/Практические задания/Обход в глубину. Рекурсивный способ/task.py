from typing import Hashable, List
import networkx as nx
from matplotlib import pyplot as plt

def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    ...  # TODO реализовать обход в глубину
    visited=set()
    result_path=[]

    def recursion(node):
        visited.add(node)
        result_path.append(node)
        for elem_node in g[node]:
            if elem_node not in visited:
                recursion(elem_node)
    recursion(start_node)
    return result_path

if __name__ == '__main__':
    # TODO записать граф с помощью модуля networkx и прверить обход в ширину
    graph = nx.Graph()
    graph.add_nodes_from('ABFGCED')
    graph.add_edges_from([('A','C'),
                          ('A','B'),
                          ('C','F'),
                          ('B','E'),
                          ('B','D'),
                          ('E','G')])
    # nx.draw_spring(graph,node_color='purple',node_size=1000,with_labels=True)
    # plt.show()
    print(dfs(graph,'A'))
