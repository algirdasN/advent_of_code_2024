import re


def main():
    with open("data/19.txt") as file:
        data = file.read().split("\n\n")

    towels = data[0].split(", ")
    designs = data[1].split()

    basic_towels = []
    for t in towels:
        for i in range(len(t)):
            if t[:i] in towels and t[i:] in towels:
                break
        else:
            basic_towels.append(t)

    pattern = re.compile("^(" + "|".join(basic_towels) + ")+$")

    print(sum(pattern.fullmatch(x) is not None for x in designs))


if __name__ == "__main__":
    main()
