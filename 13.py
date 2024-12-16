import re

PATTERN = re.compile("X[+=](\d+), Y[+=](\d+)")


def main():
    with open("data/13.txt") as file:
        games = file.read().split("\n\n")

    cost_a = 3
    cost_b = 1

    total = 0
    for game in games:
        a, b, prize = game.split("\n")
        ax, ay = (int(x) for x in PATTERN.search(a).groups())
        bx, by = (int(x) for x in PATTERN.search(b).groups())
        prize_x, prize_y = (int(x) for x in PATTERN.search(prize).groups())

        count_a = 0
        count_b = min(prize_x // bx, prize_y // by)
        temp_x = count_b * bx
        temp_y = count_b * by

        while temp_x != prize_x or temp_y != prize_y:
            if count_b == 0:
                break

            if temp_x > prize_x or temp_y > prize_y:
                count_b -= 1
                temp_x -= bx
                temp_y -= by
            else:
                count_a += 1
                temp_x += ax
                temp_y += ay
        else:
            total += count_a * cost_a + count_b * cost_b

    print(total)


if __name__ == "__main__":
    main()
