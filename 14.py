import re

PATTERN = re.compile("p=(\d+),(\d+) v=(-?\d+),(-?\d+)")


def check_tree(robots, max_x, max_y, max_stragglers):
    stragglers = 0
    for r in robots:
        if not check_neighbors(robots, r, max_x, max_y):
            stragglers += 1
            if stragglers > max_stragglers:
                break

    return stragglers


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

    min_stragglers = len(robots)
    min_second = 0

    for i in range(1, max_x * max_y):
        positions = set()
        for px, py, vx, vy in robots:
            x = (px + vx * i) % max_x
            y = (py + vy * i) % max_y
            positions.add((x, y))

        stragglers = check_tree(positions, max_x, max_y, min_stragglers)
        if stragglers < min_stragglers:
            min_stragglers = stragglers
            min_second = i

    print(min_second)


if __name__ == "__main__":
    main()
