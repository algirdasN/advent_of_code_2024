from collections import deque


def validate_half_sum_or_carry(gate_map, value, swapped):
    xor_gate_w_output = [k for k, v in gate_map.items() if {"XOR", value} <= k]
    if len(xor_gate_w_output) != 1:
        swapped.add(value)
        return

    next_output = gate_map[xor_gate_w_output[0]]
    if not next_output.startswith("z"):
        swapped.add(next_output)
        return

    and_gate_w_output = [k for k, v in gate_map.items() if {"AND", value} <= k]
    if len(and_gate_w_output) != 1:
        swapped.add(value)
        return

    next_output = gate_map[and_gate_w_output[0]]
    or_gate_w_output = [k for k, v in gate_map.items() if {"OR", next_output} <= k]
    if len(or_gate_w_output) != 1:
        swapped.add(next_output)
        return


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
    swapped = set()

    for key, value in gate_map.items():
        has_z_output = value.startswith("z")

        if "AND" in key:
            has_xy_inputs = all(map(lambda x: x == "AND" or x.startswith("x") or x.startswith("y"), key))
            if has_xy_inputs & has_z_output:
                swapped.add(value)
                continue

            if "x00" in key:
                validate_half_sum_or_carry(gate_map, value, swapped)
                continue

            or_gate_w_output = [k for k, v in gate_map.items() if {"OR", value} <= k]
            if len(or_gate_w_output) != 1:
                swapped.add(value)
                continue

        if "XOR" in key:
            has_xy_inputs = all(map(lambda x: x == "XOR" or x.startswith("x") or x.startswith("y"), key))

            if "x00" in key:
                if value != "z00":
                    swapped.add(value)
                continue

            if not (has_xy_inputs ^ has_z_output):
                swapped.add(value)
                continue

            if has_z_output:
                continue

            validate_half_sum_or_carry(gate_map, value, swapped)

        if "OR" in key:
            if has_z_output:
                if value != "z45":
                    swapped.add(value)
                continue

            validate_half_sum_or_carry(gate_map, value, swapped)

    print(",".join(sorted(swapped)))


if __name__ == "__main__":
    main()
