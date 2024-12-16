from collections import defaultdict
from itertools import cycle, dropwhile

DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

GRID: list[str]
VISITED_DICT = defaultdict(set)
TRIED_BLOCKS = set()


def move(curr, curr_dir, dir_iter):
    next_cell = (curr[0] + curr_dir[0], curr[1] + curr_dir[1])

    if not (0 <= next_cell[0] < len(GRID) and 0 <= next_cell[1] < len(GRID[0])):
        return None

    while GRID[next_cell[0]][next_cell[1]] == "#":
        curr_dir = next(dir_iter)
        next_cell = (curr[0] + curr_dir[0], curr[1] + curr_dir[1])

    return next_cell, curr_dir


def check_block(curr, curr_dir, block_cell):
    if block_cell in TRIED_BLOCKS or GRID[block_cell[0]][block_cell[1]] == "#":
        return False

    TRIED_BLOCKS.add(block_cell)
    GRID[block_cell[0]][block_cell[1]] = "#"

    new_visited_dict = defaultdict(set)
    dir_iter = dropwhile(lambda x: x != curr_dir, cycle(DIRS))
    curr_dir = next(dir_iter)
    while True:
        if curr in VISITED_DICT[curr_dir] or curr in new_visited_dict[curr_dir]:
            has_loop = True
            break

        new_visited_dict[curr_dir].add(curr)

        move_result = move(curr, curr_dir, dir_iter)

        if move_result is None:
            has_loop = False
            break

        (curr, curr_dir) = move_result

    GRID[block_cell[0]][block_cell[1]] = "."
    return has_loop


def main():
    global GRID

    with open("data/06.txt") as file:
        GRID = [list(x) for x in file.read().split()]

    start = (-1, -1)
    for i in range(len(GRID)):
        for j in range(len(GRID[i])):
            if GRID[i][j] == "^":
                start = (i, j)

    total_loops = 0
    curr = start
    dir_iter = cycle(DIRS)
    curr_dir = next(dir_iter)
    while True:
        move_result = move(curr, curr_dir, dir_iter)

        if move_result is None:
            VISITED_DICT[curr_dir].add(curr)
            break

        (next_cell, curr_dir) = move_result

        total_loops += check_block(curr, curr_dir, next_cell)
        VISITED_DICT[curr_dir].add(curr)
        curr = next_cell

    print(len(set().union(*VISITED_DICT.values())))
    print(total_loops)


if __name__ == "__main__":
    main()
