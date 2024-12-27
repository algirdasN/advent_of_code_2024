from collections import deque, Counter


def generate(num):
    num = (num << 6 ^ num) & 0xFFFFFF
    num = (num >> 5 ^ num) & 0xFFFFFF
    num = (num << 11 ^ num) & 0xFFFFFF
    return num


def main():
    with open("data/22.txt") as file:
        secret_numbers = [int(x) for x in file.read().splitlines()]

    number_total = 0
    sequence_counter = Counter()
    for num in secret_numbers:
        changes = deque(maxlen=4)
        monkey_sequences = {}
        for i in range(2000):
            new_num = generate(num)
            changes.append(new_num % 10 - num % 10)
            t = tuple(changes)
            if len(t) == 4 and t not in monkey_sequences:
                monkey_sequences[t] = new_num % 10
            num = generate(num)
        number_total += num
        sequence_counter.update(monkey_sequences)

    print(number_total)
    print(sequence_counter.most_common(1)[0][1])


if __name__ == "__main__":
    main()
