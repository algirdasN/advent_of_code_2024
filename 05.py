from collections import defaultdict


def main():
    with open("data/05.txt") as file:
        rules, updates = (x.split() for x in file.read().split("\n\n"))

    rule_dict = defaultdict(list)
    for r in rules:
        temp = r.split("|")
        rule_dict[temp[0]].append(temp[1])

    total = 0
    for pages in updates:
        p = pages.split(",")
        for i in range(len(p) - 1, 0, -1):
            if set(p[:i]) & set(rule_dict[p[i]]):
                break
        else:
            total += int(p[len(p) // 2])

    print(total)


if __name__ == "__main__":
    main()