from collections import defaultdict


def check_loop(graph, path, curr) -> set:
    result = set()
    if len(path) == 3:
        if path[0] == curr:
            result.add(frozenset(path))
        return result

    path = path + [curr]
    for next_comp in graph[path[-1]]:
        result |= check_loop(graph, path, next_comp)

    return result


def main():
    with open("data/23.txt") as file:
        data = file.read().split()

    graph = defaultdict(list)
    t_computers = set()
    for pair in data:
        c1, c2 = pair.split("-")

        graph[c1].append(c2)
        graph[c2].append(c1)

        if c1[0] == "t":
            t_computers.add(c1)
        if c2[0] == "t":
            t_computers.add(c2)

    computer_sets = set()
    for comp in t_computers:
        computer_sets |= check_loop(graph, [], comp)

    print(len(computer_sets))

    computer_sets = set(frozenset(x.split("-")) for x in data)
    while len(computer_sets) > 1:
        next_sets = set()
        for comp_set in computer_sets:
            common_neighbours = None
            for comp in comp_set:
                if common_neighbours is None:
                    common_neighbours = set(graph[comp])
                else:
                    common_neighbours &= set(graph[comp])

            for neighbour in common_neighbours:
                next_sets.add(frozenset(comp_set | {neighbour}))

        computer_sets = next_sets

    print(",".join(sorted(list(computer_sets.pop()))))


if __name__ == "__main__":
    main()
