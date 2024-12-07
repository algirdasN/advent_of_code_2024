from collections import defaultdict

RULE_DICT = defaultdict(list)

def check_pages(pages):
    for i in range(len(pages) - 1, 0, -1):
        if set(pages[:i]) & set(RULE_DICT[pages[i]]):
            return False
    return True

def fix_pages(pages, last_index = None):
    if last_index is None:
        last_index = len(pages) - 1

    for i in range(last_index, 0, -1):
        for j in range(i - 1, -1, -1):
            if pages[j] in RULE_DICT[pages[i]]:
                pages[i], pages[j] = pages[j], pages[i]
                fix_pages(pages, i)
                return

def main():
    with open("data/05.txt") as file:
        rules, updates = (x.split() for x in file.read().split("\n\n"))

    for r in rules:
        temp = r.split("|")
        RULE_DICT[temp[0]].append(temp[1])

    total = 0
    total_fixed = 0
    for pages in updates:
        p = pages.split(",")
        valid = check_pages(p)

        if valid:
            total += int(p[len(p) // 2])
        else:
            fix_pages(p)
            total_fixed += int(p[len(p) // 2])

    print(total)
    print(total_fixed)

if __name__ == "__main__":
    main()