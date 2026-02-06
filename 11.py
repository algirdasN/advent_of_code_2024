from collections import defaultdict


def walk(mappings, stone, rem_moves):
    if rem_moves == 0:
        return 1

    if stone in mappings and rem_moves in mappings[stone]:
        return mappings[stone][rem_moves]

    num_str = str(stone)
    if len(num_str) % 2 == 0:
        index = len(num_str) // 2
        new1 = int(num_str[:index])
        new2 = int(num_str[index:])
        total = walk(mappings, new1, rem_moves - 1) + walk(mappings, new2, rem_moves - 1)
    else:
        new = stone * 2024 if stone else 1
        total = walk(mappings, new, rem_moves - 1)

    mappings[stone][rem_moves] = total

    return total


def main():
    with open("data/11.txt") as file:
        stones = [int(x) for x in file.read().split()]

    mappings = defaultdict(dict)

    print(sum(walk(mappings, x, 25) for x in stones))
    print(sum(walk(mappings, x, 75) for x in stones))


if __name__ == "__main__":
    main()
