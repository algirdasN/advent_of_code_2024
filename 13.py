import re

PATTERN = re.compile("X[+=](\d+), Y[+=](\d+)")


def main():
    with open("data/13.txt") as file:
        games = file.read().split("\n\n")

    total_simple = 0
    total_complex = 0
    for game in games:
        a, b, prize = game.split("\n")
        ax, ay = (int(x) for x in PATTERN.search(a).groups())
        bx, by = (int(x) for x in PATTERN.search(b).groups())
        prize_x, prize_y = (int(x) for x in PATTERN.search(prize).groups())

        denom = ax * by - ay * bx

        if denom != 0:
            num_a = prize_x * by - prize_y * bx
            num_b = ax * prize_y - ay * prize_x

            if num_a % denom == 0 and num_b % denom == 0:
                a = num_a // denom
                b = num_b // denom
                total_simple += 3 * a + b

            prize_x += 10000000000000
            prize_y += 10000000000000

            num_a = prize_x * by - prize_y * bx
            num_b = ax * prize_y - ay * prize_x

            if num_a % denom == 0 and num_b % denom == 0:
                a = num_a // denom
                b = num_b // denom
                total_complex += 3 * a + b

    print(total_simple)
    print(total_complex)


if __name__ == "__main__":
    main()
