DIRS = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

EMPTY = "."
BOX = "O"
WALL = "#"


def main():
    with open("data/15.txt") as file:
        grid, moves = file.read().split("\n\n")

    grid = [list(x) for x in grid.split()]
    moves = moves.replace("\n", "")

    curr = (-1, -1)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                grid[i][j] = EMPTY
                curr = (i, j)

    for move in moves:
        curr_dir = DIRS[move]
        next_cell = (curr[0] + curr_dir[0], curr[1] + curr_dir[1])

        if grid[next_cell[0]][next_cell[1]] == EMPTY:
            curr = next_cell
            continue

        if grid[next_cell[0]][next_cell[1]] == WALL:
            continue

        temp = next_cell

        while grid[temp[0]][temp[1]] == BOX:
            temp = (temp[0] + curr_dir[0], temp[1] + curr_dir[1])

        if grid[temp[0]][temp[1]] == EMPTY:
            grid[next_cell[0]][next_cell[1]] = EMPTY
            grid[temp[0]][temp[1]] = BOX
            curr = next_cell

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == BOX:
                total += 100 * i + j

    print(total)


if __name__ == "__main__":
    main()
