from collections import deque

DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]


def walk(byte_list, byte_count):
    grid_len = 70
    walls = set(byte_list[:byte_count])

    visited = set()
    queue = deque()
    queue.append(((0, 0), []))

    while queue:
        curr, path = queue.popleft()

        if curr in visited:
            continue

        if curr == (grid_len, grid_len):
            return len(path)

        visited.add(curr)

        for d in DIRS:
            next_cell = curr[0] + d[0], curr[1] + d[1]
            if 0 <= next_cell[0] <= grid_len and 0 <= next_cell[1] <= grid_len and next_cell not in walls:
                queue.append((next_cell, path + [curr]))

    return None


def main():
    with open("data/18.txt") as file:
        byte_list = [eval(x) for x in file.read().splitlines()]

    print(walk(byte_list, 1024))

    for i in range(len(byte_list) - 1, 0, -1):
        if walk(byte_list, i) is not None:
            print(",".join(str(x) for x in byte_list[i]))
            break


if __name__ == "__main__":
    main()
