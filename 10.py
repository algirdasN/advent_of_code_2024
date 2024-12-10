DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]


def main():
    with open("data/10.txt") as file:
        grid = [[int(y) for y in x] for x in file.read().splitlines()]

    peaks = set()
    score = 0
    rating = 0

    def walk(curr):
        nonlocal rating
        if grid[curr[0]][curr[1]] == 9:
            rating += 1
            peaks.add(curr)

        for d in DIRS:
            next_ = (curr[0] + d[0], curr[1] + d[1])
            if 0 <= next_[0] < len(grid) and 0 <= next_[1] < len(grid[0]) \
                    and grid[curr[0]][curr[1]] + 1 == grid[next_[0]][next_[1]]:
                walk(next_)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 0:
                continue

            peaks.clear()
            walk((i, j))
            score += len(peaks)

    print(score)
    print(rating)


if __name__ == "__main__":
    main()
