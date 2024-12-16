import re

PATTERN = re.compile("p=(\d+),(\d+) v=(-?\d+),(-?\d+)")


def main():
    with open("data/14.txt") as file:
        robots = file.read().splitlines()

    max_x = 101
    max_y = 103
    seconds = 100

    q1 = q2 = q3 = q4 = 0
    for r in robots:
        px, py, vx, vy = (int(x) for x in PATTERN.search(r).groups())

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


if __name__ == "__main__":
    main()
