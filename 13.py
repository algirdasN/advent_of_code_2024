import re

import sympy as sp
from sympy import Eq

PATTERN = re.compile("X[+=](\d+), Y[+=](\d+)")


def main():
    with open("data/13.txt") as file:
        games = file.read().split("\n\n")

    count_a, count_b = sp.Symbol("count_a", integer=True), sp.Symbol("count_b", integer=True)

    total_simple = 0
    total_complex = 0
    for game in games:
        a, b, prize = game.split("\n")
        ax, ay = (int(x) for x in PATTERN.search(a).groups())
        bx, by = (int(x) for x in PATTERN.search(b).groups())
        prize_x, prize_y = (int(x) for x in PATTERN.search(prize).groups())

        equations = [
            Eq(ax * count_a + bx * count_b, prize_x),
            Eq(ay * count_a + by * count_b, prize_y)
        ]

        solution = sp.solve(equations, count_a, count_b)
        if solution:
            total_simple += 3 * solution[count_a] + solution[count_b]

        equations = [
            Eq(ax * count_a + bx * count_b, prize_x + 10000000000000),
            Eq(ay * count_a + by * count_b, prize_y + 10000000000000)
        ]

        solution = sp.solve(equations, count_a, count_b)
        if solution:
            total_complex += 3 * solution[count_a] + solution[count_b]

    print(total_simple)
    print(total_complex)


if __name__ == "__main__":
    main()
