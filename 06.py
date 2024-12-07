from collections import defaultdict
from copy import deepcopy
from itertools import cycle

DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]


def main():
    with open("data/06.txt") as file:
        grid = [list(x) for x in file.read().split()]

    start = (-1, -1)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                start = (i, j)

    visited = set()

    curr = start
    dir_iter = cycle(DIRS)
    curr_dir = next(dir_iter)
    while True:
        visited.add(curr)
        next_cell = (curr[0] + curr_dir[0], curr[1] + curr_dir[1])

        if not (0 <= next_cell[0] < len(grid) and 0 <= next_cell[1] < len(grid[0])):
            break

        while grid[next_cell[0]][next_cell[1]] == "#":
            curr_dir = next(dir_iter)
            next_cell = (curr[0] + curr_dir[0], curr[1] + curr_dir[1])

        curr = next_cell

    print(len(visited))

    visited.discard(start)

    total = 0
    for block_cell in visited:
        grid_copy = deepcopy(grid)
        grid_copy[block_cell[0]][block_cell[1]] = "#"

        visited_dict = defaultdict(set)

        curr = start
        dir_iter = cycle(DIRS)
        curr_dir = next(dir_iter)
        while True:
            if curr in visited_dict[curr_dir]:
                total += 1
                break

            visited_dict[curr_dir].add(curr)
            next_cell = (curr[0] + curr_dir[0], curr[1] + curr_dir[1])

            if not (0 <= next_cell[0] < len(grid_copy) and 0 <= next_cell[1] < len(grid_copy[0])):
                break

            while grid_copy[next_cell[0]][next_cell[1]] == "#":
                curr_dir = next(dir_iter)
                next_cell = (curr[0] + curr_dir[0], curr[1] + curr_dir[1])

            curr = next_cell

    print(total)


if __name__ == "__main__":
    main()
