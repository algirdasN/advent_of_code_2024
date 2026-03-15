def main():
    with open("data/25.txt") as file:
        patterns = file.read().split("\n\n")

    width = patterns[0].index("\n")
    depth = patterns[0].count("\n") + 1

    keys = []
    locks = []

    for p in patterns:
        pins = []
        for i in range(width):
            pins.append(p[i:len(p):width + 1].count("#"))

        if p.startswith("#####"):
            keys.append(pins)
        else:
            locks.append(pins)

    total = 0
    for k in keys:
        for p in locks:
            for i in range(width):
                if k[i] + p[i] > depth:
                    break
            else:
                total += 1

    print(total)


if __name__ == "__main__":
    main()
