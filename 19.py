def solve_pattern(towels, design_map, design):
    if design == "":
        return 1

    if design in design_map:
        return design_map[design]

    total = 0

    for t in towels:
        if design.startswith(t):
            total += solve_pattern(towels, design_map, design[len(t):])

    design_map[design] = total

    return total


def main():
    with open("data/19.txt") as file:
        data = file.read().split("\n\n")

    towels = data[0].split(", ")
    designs = data[1].split()

    design_map = {}
    possible = 0
    combinations = 0
    for d in designs:
        count = solve_pattern(towels, design_map, d)
        possible += count > 0
        combinations += count

    print(possible)
    print(combinations)


if __name__ == "__main__":
    main()
