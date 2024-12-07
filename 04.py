def rotate(matrix):
    new_matrix = []
    for i in range(len(matrix) * 2 - 1):
        new_line = ""
        for j in range(i + 1):
            if i - j < len(matrix) and j < len(matrix):
                new_line += matrix[i - j][j]
        new_matrix.append(new_line)

    return new_matrix

def main():
    with open("data/04.txt") as file:
        lines = file.read().splitlines()

    transposed_lines = list("".join(l) for l in zip(*lines))
    right_rotation = rotate(lines)
    left_rotation = rotate([l[::-1] for l in lines])

    print(
        sum(l.count("XMAS") for l in lines) +
        sum(l.count("SAMX") for l in lines) +
        sum(l.count("XMAS") for l in transposed_lines) +
        sum(l.count("SAMX") for l in transposed_lines) +
        sum(l.count("XMAS") for l in right_rotation) +
        sum(l.count("SAMX") for l in right_rotation) +
        sum(l.count("XMAS") for l in left_rotation) +
        sum(l.count("SAMX") for l in left_rotation)
    )

    total = 0
    valid = ["MAS", "SAM"]
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            if lines[i][j] != "A":
                continue

            diagonal1 = lines[i - 1][j - 1] + "A" + lines[i + 1][j + 1]
            diagonal2 = lines[i - 1][j + 1] + "A" + lines[i + 1][j - 1]

            if diagonal1 in valid and diagonal2 in valid:
                total += 1

    print(total)

if __name__ == "__main__":
    main()