#!/usr/bin/env python3
"""
Convert an adjacency matrix to an adjacency list, print edges,
and detect simple structures (e.g. cycle of length 4) for the
example question.

Usage: run without args to use the example matrix from the question.
"""
from collections import deque
import ast
import sys


def matrix_to_adj_list(matrix):
    n = len(matrix)
    adj = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                adj[i].append(j)
    return adj


def edges_from_adj(adj):
    # For undirected graphs represented by symmetric matrices,
    # list each undirected edge once (i < j).
    edges = []
    for u in adj:
        for v in adj[u]:
            if u <= v:
                edges.append((u, v))
    return edges


def is_connected(adj, start=0):
    visited = set()
    q = deque([start])
    while q:
        node = q.popleft()
        if node in visited:
            continue
        visited.add(node)
        for nbr in adj.get(node, []):
            if nbr not in visited:
                q.append(nbr)
    return len(visited) == len(adj)


def is_cycle_of_length_n(adj, n):
    # Simple check: each node degree == 2 and connected and node count == n
    if len(adj) != n:
        return False
    for u in adj:
        if len(adj[u]) != 2:
            return False
    return is_connected(adj, start=next(iter(adj)))


def main(matrix=None):
    if matrix is None:
        matrix = [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
        ]

    adj = matrix_to_adj_list(matrix)
    print('Adjacency list:')
    for k in sorted(adj):
        print(f'  {k}: {adj[k]}')

    # Detect undirected edges (avoid duplicates)
    undirected_edges = []
    seen = set()
    for u in adj:
        for v in adj[u]:
            if (v, u) not in seen:
                undirected_edges.append((u, v))
                seen.add((u, v))
                seen.add((v, u))

    print('\nEdges (undirected listing):')
    for u, v in undirected_edges:
        print(f'  {u} - {v}')

    # Check if this is a 4-cycle (square)
    if is_cycle_of_length_n(adj, 4):
        print('\nStructure detected: 4-cycle (square).')
    else:
        print('\nStructure detected: not a 4-cycle (square).')


if __name__ == '__main__':
    # If the user provides a matrix literal on the command line, parse it
    if len(sys.argv) >= 2:
        try:
            matrix = ast.literal_eval(sys.argv[1])
        except Exception as e:
            print('Unable to parse matrix literal:', e)
            sys.exit(1)
        main(matrix)
    else:
        main()
