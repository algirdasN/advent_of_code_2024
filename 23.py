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


if __name__ == "__main__":
    main()
