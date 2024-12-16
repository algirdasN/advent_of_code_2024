from collections import deque
from itertools import count


def main():
    with open("data/11.txt") as file:
        stones = deque((int(x), 0) for x in file.read().split())

    max_moves = 25
    total = 0
    mapping = {}
    while stones:
        (orig_number, move) = stones.pop()

        if orig_number in mapping:
            (new1, new2, i) = mapping[orig_number]
            if move + i < max_moves:
                stones.append((new1, move + i))
                stones.append((new2, move + i))
            else:
                total += 2 if move + i == max_moves else 1
            continue

        number = orig_number
        for i in count(1):
            if move + i > max_moves:
                total += 1
                break

            num_str = str(number)
            if len(num_str) % 2 == 0:
                index = len(num_str) // 2
                new1 = int(num_str[:index])
                new2 = int(num_str[index:])
                mapping[orig_number] = (new1, new2, i)
                stones.append((new1, move + i))
                stones.append((new2, move + i))
                break

            number = number * 2024 if number else 1

    print(total)


if __name__ == "__main__":
    main()
