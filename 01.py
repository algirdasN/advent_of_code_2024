def main():
    with open("data/01.txt") as file:
        left, right = zip(*[[int(val) for val in line.split()] for line in file.readlines()])

    distances = [abs(x[0] - x[1]) for x in zip(sorted(left), sorted(right))]
    print(sum(distances))

    similarity = sum(x * right.count(x) for x in left)
    print(similarity)

if __name__ == "__main__":
    main()