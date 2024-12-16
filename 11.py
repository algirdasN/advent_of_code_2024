from collections import deque


def main():
    with open("data/11.txt") as file:
        stones = deque((int(x), 0) for x in file.read().split())

    max_moves = 25
    total = 0
    while stones:
        (number, move) = stones.pop()

        if move >= max_moves:
            total += 1
            continue

        num_str = str(number)

        if len(num_str) % 2 == 0:
            index = len(num_str) // 2
            stones.append((int(num_str[index:]), move + 1))
            stones.append((int(num_str[:index]), move + 1))
        elif number == 0:
            stones.append((1, move + 1))
        else:
            stones.append((number * 2024, move + 1))

    print(total)


if __name__ == "__main__":
    main()
