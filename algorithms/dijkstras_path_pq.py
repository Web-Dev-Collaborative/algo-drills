"""
ID: b23383a0-792a-47e9-a13c-fe4f2417f909
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Using_a_priority_queue
Instead of decreasing priority, just always add it and check if it's visited.
The output from this function will work with backpedal.py.
"""
from collections.abc import Mapping
from heapq import heappop, heappush
from math import inf
from numbers import Real
from typing import Optional

from hints import Node


def dijkstras_path_pq(
    graph: Mapping[Node, Mapping[Node, Real]],
    start: Node,
    goal: Node
) -> tuple[dict[Node, Real], dict[Node, Optional[Node]]]:
    """Find the shortest path from start to goal in a directed, weighted graph. Return it as a parents dict."""
    distances = dict.fromkeys(graph, inf)
    distances[start] = 0
    parents = dict.fromkeys(graph)
    unvisited = set(graph)
    pq = [(0, start)]
    while pq:
        distance, node = heappop(pq)
        if node not in unvisited:
            continue
        unvisited.remove(node)
        if node == goal:
            break
        for next_node, weight in graph[node].items():
            next_distance = distance + weight
            if next_distance < distances[next_node]:
                distances[next_node] = next_distance
                parents[next_node] = node
                heappush(pq, (next_distance, next_node))
    return distances, parents
