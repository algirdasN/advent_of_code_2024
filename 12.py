from collections import defaultdict

DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]


def main():
    with open("data/12.txt") as file:
        grid = [list(x) for x in file.read().splitlines()]

    x_len = len(grid)
    y_len = len(grid)

    visited = [[False] * y_len for _ in range(x_len)]
    fence = defaultdict(set)

    def walk(x, y):
        steps = 1
        symbol = grid[x][y]
        visited[x][y] = True

        for d in DIRS:
            new_x = x + d[0]
            new_y = y + d[1]

            if (0 <= new_x < x_len and 0 <= new_y < y_len) and grid[new_x][new_y] == symbol:
                if not visited[new_x][new_y]:
                    steps += walk(new_x, new_y)
            else:
                fence[d].add((new_x, new_y))

        return steps

    total = 0
    total_adv = 0
    for i in range(x_len):
        for j in range(y_len):
            if visited[i][j]:
                continue

            fence.clear()
            area = walk(i, j)

            total += area * sum(len(x) for x in fence.values())

            sides = 0
            for direction, coordinates in fence.items():
                index = 1 if direction[0] == 0 else 0
                coord_dict = defaultdict(list)
                for xy in coordinates:
                    coord_dict[xy[index]].append(xy[not index])

                for pieces in coord_dict.values():
                    pieces.sort()
                    sides += 1
                    for p in range(len(pieces) - 1):
                        if pieces[p] + 1 != pieces[p + 1]:
                            sides += 1

            total_adv += area * sides

    print(total)
    print(total_adv)


if __name__ == "__main__":
    main()
