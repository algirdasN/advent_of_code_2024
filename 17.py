import re


def run_program(program, a, b, c):
    pointer = 0
    output = []

    def combo(operand):
        match operand:
            case 4:
                return a
            case 5:
                return b
            case 6:
                return c
            case _:
                return operand

    while pointer < len(program):
        inst, data = program[pointer:pointer + 2]

        match inst:
            case 0:
                a >>= combo(data)
            case 1:
                b ^= data
            case 2:
                b = combo(data) % 8
            case 3:
                if a > 0:
                    pointer = data
                    continue
            case 4:
                b ^= c
            case 5:
                output.append(str(combo(data) % 8))
            case 6:
                b = a >> combo(data)
            case 7:
                c = a >> combo(data)

        pointer += 2

    return output


def main():
    with open("data/17.txt") as file:
        registers, prog_str = file.read().split("\n\n")

    prog_str = prog_str.split(" ")[-1].split(",")

    program = [int(x) for x in prog_str]
    a, b, c = (int(x) for x in re.findall(r"(\d+)", registers))

    output = run_program(program, a, b, c)

    print(",".join(output))

    valid = [0]

    for i in range(1, len(program) + 1):
        new_valid = []
        for j in range(8):
            for k in valid:
                a = (j << 3 * (len(program) - i)) + k
                output = run_program(program, a, b, c)

                if output[-i:] == prog_str[-i:]:
                    new_valid.append(a)
        valid = new_valid

    print(min(valid))


if __name__ == "__main__":
    main()
