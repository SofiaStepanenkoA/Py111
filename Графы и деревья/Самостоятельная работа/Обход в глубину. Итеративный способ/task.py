from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    visited = set()
    stack = [start_node]
    visit_order = []
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            visit_order.append(current_node)
            for neighbor in reversed(list(g.neighbors(current_node))):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visit_order
