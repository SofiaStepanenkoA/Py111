from typing import List
import networkx as nx

def build_trie_graph(dictionary: List[str]) -> nx.DiGraph:
    G = nx.DiGraph()
    for root in dictionary:
        current_node = ''
        for char in root:
            next_node = current_node + char
            if not G.has_edge(current_node, next_node):
                G.add_edge(current_node, next_node)
            current_node = next_node
        # Маркируем конечный узел корня
        G.nodes[current_node]['is_root'] = True
    return G

def find_root(word: str, G: nx.DiGraph) -> str:
    current_node = ''
    for i, char in enumerate(word):
        next_node = current_node + char
        if next_node in G:
            if 'is_root' in G.nodes[next_node]:
                return word[:i+1]
            current_node = next_node
        else:
            break
    return word

def replace_words(dictionary: List[str], sentence: str) -> str:
    G = build_trie_graph(dictionary)
    words = sentence.split()
    replaced_words = [find_root(word, G) for word in words]
    return ' '.join(replaced_words)