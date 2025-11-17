#!/usr/bin/env python3
"""
Simple BFS traversal helper for the CodePath question.

Graph example used in the question:
graph = {
    'A': ['B', 'D'],
    'B': ['C'],
    'C': ['D'],
    'D': ['E'],
    'E': ['F'],
    'F': []
}

BFS starting at 'A' produces: ['A', 'B', 'D', 'C', 'E', 'F']
"""

from collections import deque
import sys


def bfs(graph, start):
    """Return BFS traversal order (list) from `start` over adjacency-list `graph`.

    `graph` is expected to be a dict mapping node -> iterable of neighbors.
    """
    if start not in graph:
        return []

    visited = set([start])
    order = []
    q = deque([start])

    while q:
        node = q.popleft()
        order.append(node)
        for nbr in graph.get(node, []):
            if nbr not in visited:
                visited.add(nbr)
                q.append(nbr)

    return order


def _example():
    graph = {
        'A': ['B', 'D'],
        'B': ['C'],
        'C': ['D'],
        'D': ['E'],
        'E': ['F'],
        'F': []
    }
    print(bfs(graph, 'A'))


if __name__ == '__main__':
    # If run without arguments, print the example traversal.
    if len(sys.argv) == 1:
        _example()
    else:
        # Allow running with a simple one-line python dict input: python bfs_traversal.py "{'A':['B']},'A'"
        try:
            # Expect two args: graph_literal start
            graph_literal = sys.argv[1]
            start = sys.argv[2]
            import ast
            graph = ast.literal_eval(graph_literal)
            print(bfs(graph, start))
        except Exception as e:
            print('Usage: bfs_traversal.py [graph_literal start]')
            print('Example: python bfs_traversal.py "{\'A\':[\'B\', \'D\'], \'B\':[\'C\']}" A')
            raise
