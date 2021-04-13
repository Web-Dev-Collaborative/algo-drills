from collections import deque
from collections.abc import Sequence


def bfs_search_grid(grid: Sequence[Sequence[int]], start: tuple[int, int], goal: tuple[int, int]) -> bool:
    rows = range(len(grid))
    cols = range(len(grid[0]))
    visited = {start}
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        if (r, c) == goal:
            return True
        adjacent = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for next_node in adjacent:
            r1, c1 = next_node
            if r1 in rows and c1 in cols and grid[r1][c1] and next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
    return False
