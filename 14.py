import re
from itertools import count

PATTERN = re.compile("p=(\d+),(\d+) v=(-?\d+),(-?\d+)")


def draw_grid(robots, max_x, max_y):
    for i in range(max_x):
        row = ""
        for j in range(max_y):
            row += "#" if (i, j) in robots else "."
        print(row)


def check_tree(robots, max_x, max_y, max_stragglers):
    for r in robots:
        if not check_neighbors(robots, r, max_x, max_y):
            max_stragglers -= 1
            if max_stragglers == 0:
                return False

    return True


def check_neighbors(robots, robot, max_x, max_y):
    for i in range(max(0, robot[0] - 1), min(max_x, robot[0] + 2)):
        for j in range(max(0, robot[1] - 1), min(max_y, robot[1] + 2)):
            if (i, j) != robot and (i, j) in robots:
                return True

    return False


def main():
    with open("data/14.txt") as file:
        robots = [tuple(int(x) for x in PATTERN.search(r).groups()) for r in file.read().splitlines()]

    max_x = 101
    max_y = 103
    seconds = 100

    q1 = q2 = q3 = q4 = 0
    for px, py, vx, vy in robots:
        final_x = (px + vx * seconds) % max_x
        final_y = (py + vy * seconds) % max_y

        if final_x == max_x // 2 or final_y == max_y // 2:
            continue

        if final_x < max_x // 2:
            if final_y < max_y // 2:
                q1 += 1
            else:
                q2 += 1
        else:
            if final_y < max_y // 2:
                q3 += 1
            else:
                q4 += 1

    print(q1 * q2 * q3 * q4)

    max_stragglers = 200

    for i in count(1):
        positions = set()
        for px, py, vx, vy in robots:
            x = (px + vx * i) % max_x
            y = (py + vy * i) % max_y
            positions.add((x, y))

        if check_tree(positions, max_x, max_y, max_stragglers):
            draw_grid(positions, max_x, max_y)
            print(i)
            break


if __name__ == "__main__":
    main()
