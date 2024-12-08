from collections import defaultdict
from itertools import permutations


def main():
    with open("data/08.txt") as file:
        grid = file.read().splitlines()

    antennas = defaultdict(set)
    x_len = len(grid)
    y_len = len(grid[0])
    for i in range(x_len):
        for j in range(y_len):
            if grid[i][j] != ".":
                antennas[grid[i][j]].add((i, j))

    antinodes = set()
    for values in antennas.values():
        pairs = permutations(values, 2)
        for node1, node2 in pairs:
            x_diff = node1[0] - node2[0]
            y_diff = node1[1] - node2[1]
            antinode1 = (node1[0] + x_diff, node1[1] + y_diff)
            antinode2 = (node2[0] - x_diff, node2[1] - y_diff)

            if 0 <= antinode1[0] < x_len and 0 <= antinode1[1] < y_len:
                antinodes.add(antinode1)

            if 0 <= antinode2[0] < x_len and 0 <= antinode2[1] < y_len:
                antinodes.add(antinode2)

    print(len(antinodes))


if __name__ == "__main__":
    main()
