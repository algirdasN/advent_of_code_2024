from collections import deque

DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]


def main():
    with open("data/18.txt") as file:
        byte_list = [eval(x) for x in file.read().splitlines()]

    grid_len = 70
    byte_count = 1024

    walls = set(byte_list[:byte_count])

    visited = set()
    queue = deque()
    queue.append(((0, 0), []))

    while queue:
        curr, path = queue.popleft()

        if curr in visited:
            continue

        if curr == (grid_len, grid_len):
            print(len(path))
            break

        visited.add(curr)

        for d in DIRS:
            next_cell = curr[0] + d[0], curr[1] + d[1]
            if 0 <= next_cell[0] <= grid_len and 0 <= next_cell[1] <= grid_len and next_cell not in walls:
                queue.append((next_cell, path + [curr]))


if __name__ == "__main__":
    main()
