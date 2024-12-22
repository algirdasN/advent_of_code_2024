import heapq
import sys
from collections import deque

DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]


class Node:
    def __init__(self, x: int, y: int, d: tuple[int, int]):
        self.xy = (x, y)
        self.d = d
        self.dist = sys.maxsize

    def __lt__(self, other):
        return self.dist < other.dist

    def min_dist(self, dist):
        if dist < self.dist:
            self.dist = dist
            return True
        return False


def add_to_heap(node_map, heap, coordinates, direction, distance):
    next_node = node_map[coordinates][direction]

    if next_node.dist == sys.maxsize:
        heapq.heappush(heap, next_node)

    return next_node.min_dist(distance)


def walk_back(node_map, node_queue, coordinates, direction, distance):
    prev_node = node_map[coordinates][direction]
    if prev_node.dist == distance:
        node_queue.append(prev_node)


def main():
    with open("data/16.txt") as file:
        grid = file.read().splitlines()

    start = (-1, -1)
    end = (-1, -1)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                start = (i, j)
            if grid[i][j] == "E":
                end = (i, j)

    node_map: dict[tuple[int, int], dict[tuple[int, int], Node]] = {
        (i, j): {d: Node(i, j, d) for d in DIRS} for i in range(len(grid)) for j in range(len(grid[i]))
    }

    start_node = node_map[start][(0, 1)]
    start_node.dist = 0

    heap: list[Node] = [start_node]

    while heap:
        update = False
        curr: Node = heapq.heappop(heap)
        next_cell = (curr.xy[0] + curr.d[0], curr.xy[1] + curr.d[1])

        if grid[next_cell[0]][next_cell[1]] != "#":
            update = add_to_heap(node_map, heap, next_cell, curr.d, curr.dist + 1) or update

        right_dir = DIRS[(DIRS.index(curr.d) + 1) % 4]
        left_dir = DIRS[(DIRS.index(curr.d) + 3) % 4]

        update = add_to_heap(node_map, heap, curr.xy, right_dir, curr.dist + 1000) or update
        update = add_to_heap(node_map, heap, curr.xy, left_dir, curr.dist + 1000) or update

        if update:
            heapq.heapify(heap)

    min_dist = min(x.dist for x in node_map[end].values())
    print(min_dist)

    visited = set()
    node_queue = deque(x for x in node_map[end].values() if x.dist == min_dist)

    while node_queue:
        curr = node_queue.pop()
        visited.add(curr.xy)

        if curr.xy == start:
            continue

        walk_back(node_map, node_queue, (curr.xy[0] - curr.d[0], curr.xy[1] - curr.d[1]), curr.d, curr.dist - 1)

        right_dir = DIRS[(DIRS.index(curr.d) + 1) % 4]
        left_dir = DIRS[(DIRS.index(curr.d) + 3) % 4]

        walk_back(node_map, node_queue, curr.xy, right_dir, curr.dist - 1000)
        walk_back(node_map, node_queue, curr.xy, left_dir, curr.dist - 1000)

    print(len(visited))


if __name__ == "__main__":
    main()
