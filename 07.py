from itertools import product

OPERATORS = ["+", "*"]

def prepare_args(args):
    args = args.split(" ")
    args[0] = "(" * (len(args) - 1) + args[0]
    for i in range(1, len(args)):
        args[i] = args[i] + ")"
    return args

def main():
    with open("data/07.txt") as file:
        lines = file.read().splitlines()

    total = 0
    for l in lines:
        result, arguments = l.split(": ")
        result = int(result)
        arguments = prepare_args(arguments)

        op_combination = product(OPERATORS, repeat=len(arguments) - 1)

        for op in op_combination:
            expression = "".join([x for pair in zip(arguments, op) for x in pair]) + arguments[-1]
            if eval(expression) == result:
                total += result
                break

    print(total)


if __name__ == "__main__":
    main()
