from itertools import product

OPERATORS = ["+", "*"]
OPERATORS_ADV = ["+", "*", "||"]


def check_expression(arguments, operators, result):
    temp = arguments[0]

    for i in range(1, len(arguments)):
        match operators[i - 1]:
            case "+":
                temp += arguments[i]
            case "*":
                temp *= arguments[i]
            case "||":
                temp = int(str(temp) + str(arguments[i]))

        if temp > result:
            return False

    return temp == result


def main():
    with open("data/07.txt") as file:
        lines = file.read().splitlines()

    total = 0
    total_adv = 0
    for l in lines:
        result, arguments = l.split(": ")
        result = int(result)
        arguments = [int(x) for x in arguments.split(" ")]

        op_combinations = product(OPERATORS, repeat=len(arguments) - 1)

        for op in op_combinations:
            if check_expression(arguments, op, result):
                total += result
                total_adv += result
                break
        else:
            op_adv_combinations = product(OPERATORS_ADV, repeat=len(arguments) - 1)
            op_adv_combinations = [x for x in op_adv_combinations if "||" in x]

            for op in op_adv_combinations:
                if check_expression(arguments, op, result):
                    total_adv += result
                    break

    print(total)
    print(total_adv)


if __name__ == "__main__":
    main()
