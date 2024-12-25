DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

WALL = "#"


def main():
    with open("data/19.txt") as file:
        grid = file.read().splitlines()

    grid_map = {(i, j): value for i, sublist in enumerate(grid) for j, value in enumerate(sublist)}

    start = (-1, -1)
    end = (-1, -1)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                start = (i, j)
            if grid[i][j] == "E":
                end = (i, j)

    curr = start
    path = []

    while curr != end:
        path.append(curr)

        for d in DIRS:
            next_cell = curr[0] + d[0], curr[1] + d[1]
            if grid_map[next_cell] != WALL and next_cell not in path:
                curr = next_cell
                break

    path.append(end)

    total = 0
    for i in range(len(path)):
        jump_from = path[i]
        for d in DIRS:
            skip_cell = jump_from[0] + d[0], jump_from[1] + d[1]
            if grid_map[skip_cell] != WALL:
                continue

            jump_to = jump_from[0] + 2 * d[0], jump_from[1] + 2 * d[1]
            if 0 <= jump_to[0] < len(grid) and 0 <= jump_to[1] < len(grid[0]) \
                    and grid_map[jump_to] != WALL \
                    and path.index(jump_to) - i - 2 >= 100:
                total += 1

    print(total)


if __name__ == "__main__":
    main()
