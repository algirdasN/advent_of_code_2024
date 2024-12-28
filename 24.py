from collections import deque


def main():
    with open("data/24.txt") as file:
        init, gates = file.read().split("\n\n")

    for row in init.splitlines():
        exec(row.replace(":", "="))

    gate_expressions = deque()
    for gate in gates.splitlines():
        expr, result = gate.split(" -> ")
        expr = expr.replace("XOR", "^").replace("OR", "|").replace("AND", "&")
        gate_expressions.append(f"{result} = {expr}")

    while gate_expressions:
        expr = gate_expressions.popleft()
        try:
            exec(expr)
        except NameError:
            gate_expressions.append(expr)

    z_variables = [x for x in sorted(locals().items(), reverse=True) if x[0][0] == "z"]
    z_bit_values = "".join(str(x[1]) for x in z_variables)
    print(int(z_bit_values, 2))


if __name__ == "__main__":
    main()
