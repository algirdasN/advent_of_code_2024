from collections import deque


def main():
    with open("data/24.txt") as file:
        init, gates = file.read().split("\n\n")

    wires = {}

    for row in init.splitlines():
        r = row.split(":")
        wires[r[0]] = int(r[1])

    gate_expressions = []
    for gate in gates.splitlines():
        expr, result = gate.split(" -> ")
        var1, op, var2 = expr.split(" ")
        gate_expressions.append((var1, var2, op, result))

    gate_queue = deque(gate_expressions)
    while gate_queue:
        var1, var2, op, result = gate_queue.popleft()
        if var1 in wires and var2 in wires:
            match op:
                case "AND":
                    wires[result] = wires[var1] & wires[var2]
                case "OR":
                    wires[result] = wires[var1] | wires[var2]
                case "XOR":
                    wires[result] = wires[var1] ^ wires[var2]
        else:
            gate_queue.append((var1, var2, op, result))

    total = 0
    for int_sum_key in wires:
        if int_sum_key.startswith("z") and wires[int_sum_key]:
            total += 2 ** int(int_sum_key[1:])

    print(total)

    gate_map = {frozenset(x[:3]): x[3] for x in gate_expressions}

    swapped = []
    i = 1
    carry = gate_map[frozenset(("x00", "y00", "AND"))]
    while i < 45:
        x = f"x{i:02}"
        y = f"y{i:02}"
        z = f"z{i:02}"

        int_sum_key = frozenset((x, y, "XOR"))
        int_carry_key = frozenset((x, y, "AND"))

        int_sum = gate_map[int_sum_key]
        if int_sum == z:
            test_set = {carry, "XOR"}
            z_key = [x for x in gate_map if test_set <= x][0]
            actual = next(iter(z_key - test_set))
            gate_map[z_key] = int_sum
            gate_map[int_sum_key] = actual
            swapped += [int_sum, actual]
            continue

        z_key = frozenset((carry, int_sum, "XOR"))
        int_carry2_key = frozenset((carry, int_sum, "AND"))

        int_carry = gate_map[int_carry_key]  #
        if int_carry == z:
            test_set = {gate_map[int_carry2_key], "OR"}
            carry_key = [x for x in gate_map if test_set <= x][0]
            actual = next(iter(carry_key - test_set))
            gate_map[z_key] = int_carry
            gate_map[int_carry_key] = actual
            swapped += [int_carry, actual]
            continue

        if z_key not in gate_map:
            gate_map[int_carry_key] = int_sum
            gate_map[int_sum_key] = int_carry
            swapped += [int_carry, int_sum]
            continue

        if gate_map[z_key] != z:
            actual_key = [k for k, v in gate_map.items() if v == z][0]
            actual = gate_map[z_key]
            gate_map[actual_key] = actual
            gate_map[z_key] = z
            swapped += [actual, z]
            continue

        int_carry2 = gate_map[int_carry2_key]
        carry = gate_map[frozenset((int_carry, int_carry2, "OR"))]

        i += 1

    print(",".join(sorted(swapped)))

if __name__ == "__main__":
    main()
