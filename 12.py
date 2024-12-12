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

    area = 0
    perimeter = 0

    def walk(x, y):
        nonlocal area, perimeter
        symbol = grid[x][y]
        visited[x][y] = True
        area += 1

        for d in DIRS:
            new_x = x + d[0]
            new_y = y + d[1]

            if (0 <= new_x < x_len and 0 <= new_y < y_len) and grid[new_x][new_y] == symbol:
                if not visited[new_x][new_y]:
                    walk(new_x, new_y)
            else:
                perimeter += 1

    total = 0
    for i in range(x_len):
        for j in range(y_len):
            if visited[i][j]:
                continue

            area = 0
            perimeter = 0

            walk(i, j)

            total += area * perimeter

    print(total)


if __name__ == "__main__":
    main()
