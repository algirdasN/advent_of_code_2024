DIRECTIONS = {
    (-1, 0): "^",
    (0, -1): "<",
    (1, 0): "v",
    (0, 1): ">"
}

NUMPAD = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2)
}

DIRPAD = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2)
}


def valid_paths(start, end, exclude):
    paths = []
    x_diff = end[0] - start[0]
    y_diff = end[1] - start[1]

    if x_diff != 0:
        abs_diff = abs(x_diff)
        sign = int(x_diff / abs_diff)

        paths.append(DIRECTIONS[(sign, 0)] * abs_diff)

    if y_diff != 0:
        abs_diff = abs(y_diff)
        sign = int(y_diff / abs_diff)

        paths.append(DIRECTIONS[(0, sign)] * abs_diff)

    if len(paths) == 2:
        paths = [paths[0] + paths[1], paths[1] + paths[0]]
        if start[1] == exclude[1] and end[0] == exclude[0]:
            paths.pop(0)
        elif start[0] == exclude[0] and end[1] == exclude[1]:
            paths.pop(1)

    return paths


def solve_numpad(code):
    curr = NUMPAD["A"]
    paths = []
    for char in code:
        nxt = NUMPAD[char]
        nxt_paths = valid_paths(curr, nxt, (3, 0))
        if not paths:
            paths = [p + "A" for p in nxt_paths]
        elif not nxt_paths:
            paths = [p + "A" for p in paths]
        else:
            paths = [a + b + "A" for a in paths for b in nxt_paths]
        curr = nxt

    return paths


def solve_dirpad(mapping, path, depth):
    if depth == 0:
        return len(path)

    curr = DIRPAD["A"]
    total = 0
    for char in path:
        nxt = DIRPAD[char]
        if curr == nxt:
            total += 1
            continue

        key = (char, curr, depth)
        if key not in mapping:
            nxt_paths = valid_paths(curr, nxt, (0, 0))
            mapping[key] = min(solve_dirpad(mapping, p + "A", depth - 1) for p in nxt_paths)

        total += mapping[key]
        curr = nxt

    return total


def solve_code(mapping, code, robot_pads):
    paths = solve_numpad(code)

    return int(code[:-1]) * min(solve_dirpad(mapping, p, robot_pads) for p in paths)


def main():
    with open("data/21.txt") as file:
        codes = file.read().split("\n")

    mapping = {}

    print(sum(solve_code(mapping, c, 2) for c in codes))
    print(sum(solve_code(mapping, c, 25) for c in codes))


if __name__ == "__main__":
    main()
