DIRS = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

EMPTY = "."
BOX = "O"
WALL = "#"
WIDE_BOX = ("[", "]")


def play_regular(grid_str, moves):
    grid = [list(x) for x in grid_str.split()]

    curr = (-1, -1)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                grid[i][j] = EMPTY
                curr = (i, j)

    for move in moves:
        curr_dir = DIRS[move]
        curr = move_regular(grid, curr, curr_dir)

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == BOX:
                total += 100 * i + j

    return total


def move_regular(grid, curr, curr_dir):
    next_cell = (curr[0] + curr_dir[0], curr[1] + curr_dir[1])

    if grid[next_cell[0]][next_cell[1]] == EMPTY:
        return next_cell

    if grid[next_cell[0]][next_cell[1]] == WALL:
        return curr

    front = next_cell

    while grid[front[0]][front[1]] == BOX:
        front = (front[0] + curr_dir[0], front[1] + curr_dir[1])

    if grid[front[0]][front[1]] != EMPTY:
        return curr

    grid[next_cell[0]][next_cell[1]] = EMPTY
    grid[front[0]][front[1]] = BOX
    return next_cell


def play_wide(grid_str, moves):
    grid_str = grid_str.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    grid = [list(x) for x in grid_str.split()]

    curr = (-1, -1)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                grid[i][j] = EMPTY
                curr = (i, j)

    for move in moves:
        curr_dir = DIRS[move]

        if curr_dir[0] == 0:
            curr = move_wide_h(grid, curr, curr_dir)
        else:
            curr = move_wide_v(grid, curr, curr_dir)

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == WIDE_BOX[0]:
                total += 100 * i + j

    return total


def move_wide_h(grid, curr, curr_dir):
    front = (curr[0] + curr_dir[0], curr[1] + curr_dir[1])

    while grid[front[0]][front[1]] in WIDE_BOX:
        front = (front[0] + curr_dir[0], front[1] + curr_dir[1])

    if grid[front[0]][front[1]] != EMPTY:
        return curr

    while True:
        second = (front[0] - curr_dir[0], front[1] - curr_dir[1])
        grid[front[0]][front[1]] = grid[second[0]][second[1]]

        if second == curr:
            return front

        front = second


def move_wide_v(grid, curr, curr_dir):
    front = {curr}
    movable = set()
    while len(front) > 0:
        new_front = set()
        for cell in list(front):
            next_front_cell = (cell[0] + curr_dir[0], cell[1] + curr_dir[1])

            if grid[next_front_cell[0]][next_front_cell[1]] == WALL:
                return curr

            if grid[next_front_cell[0]][next_front_cell[1]] == EMPTY:
                continue

            new_front.add(next_front_cell)
            movable.add(next_front_cell)

            if grid[next_front_cell[0]][next_front_cell[1]] == WIDE_BOX[0]:
                new_front.add((next_front_cell[0], next_front_cell[1] + 1))
                movable.add((next_front_cell[0], next_front_cell[1] + 1))
            else:
                new_front.add((next_front_cell[0], next_front_cell[1] - 1))
                movable.add((next_front_cell[0], next_front_cell[1] - 1))

        front = new_front

    move_list = sorted(list(movable), key=lambda x: x[0], reverse=curr_dir[0] == 1)
    for cell in move_list:
        grid[cell[0] + curr_dir[0]][cell[1] + curr_dir[1]] = grid[cell[0]][cell[1]]
        grid[cell[0]][cell[1]] = EMPTY

    return curr[0] + curr_dir[0], curr[1] + curr_dir[1]


def main():
    with open("data/15.txt") as file:
        grid, moves = file.read().split("\n\n")

    moves = moves.replace("\n", "")

    print(play_regular(grid, moves))
    print(play_wide(grid, moves))


if __name__ == "__main__":
    main()
