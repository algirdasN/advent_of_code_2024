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

        if grid[next_cell[0]][next_cell[1]] == "#":
            curr_dir = next(dir_iter)
            curr = (curr[0] + curr_dir[0], curr[1] + curr_dir[1])
        else:
            curr = next_cell

    print(len(visited))


if __name__ == "__main__":
    main()
