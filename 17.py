import re


def main():
    with open("data/17.txt") as file:
        registers, program = file.read().split("\n\n")

    prog = eval(program.split(" ")[-1])
    a, b, c = (int(x) for x in re.findall(r"(\d+)", registers))

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

    while pointer < len(prog):
        inst, data = prog[pointer:pointer + 2]

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

    print(",".join(output))


if __name__ == "__main__":
    main()
