from typing import List
import networkx as nx


def find_judge(n: int, trust: List[List[int]]) -> int:
    if n == 1:
        return 1
    g = nx.DiGraph()
    for a, b in trust:
        g.add_edge(a, b)
    for person in range(1, n + 1):
        if g.in_degree(person) == n - 1 and g.out_degree(person) == 0:
            return person
    return -1

