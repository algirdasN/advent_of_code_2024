from itertools import count

DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

WALL = "#"


def calculate_cheats(grid_map, path, len_x, len_y, max_cheat_length, save_cutoff):
    total = 0

    for jump_from in path:
        for i in range(-max_cheat_length, max_cheat_length + 1):
            for j in range(-max_cheat_length + abs(i), max_cheat_length + 1 - abs(i)):
                jump_to = jump_from[0] + i, jump_from[1] + j
                cheat_length = (abs(i) + abs(j))

                if 0 <= jump_to[0] < len_x and 0 <= jump_to[1] < len_y \
                        and grid_map[jump_to] != WALL \
                        and path[jump_to] - path[jump_from] - cheat_length >= save_cutoff:
                    total += 1

    return total


def main():
    with open("data/19.txt") as file:
        grid = file.read().splitlines()

    len_x = len(grid)
    len_y = len(grid[0])
    grid_map = {(i, j): value for i, sublist in enumerate(grid) for j, value in enumerate(sublist)}

    start = (-1, -1)
    end = (-1, -1)
    for k, v in grid_map.items():
        if v == "S":
            start = k
        if v == "E":
            end = k

    curr = start
    path = {}

    for i in count():
        path[curr] = i

        if curr == end:
            break

        for d in DIRS:
            next_cell = curr[0] + d[0], curr[1] + d[1]
            if grid_map[next_cell] != WALL and next_cell not in path:
                curr = next_cell
                break

    print(calculate_cheats(grid_map, path, len_x, len_y, 2, 100))
    print(calculate_cheats(grid_map, path, len_x, len_y, 20, 100))


if __name__ == "__main__":
    main()
