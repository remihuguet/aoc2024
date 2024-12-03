def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    l1, l2 = [], []
    for line in lines:
        l1.append(int(line.split()[0]))
        l2.append(int(line.split()[1]))
    return l1, l2


def part1(filename):
    l1, l2 = parse_input(filename)
    l1, l2 = sorted(l1), sorted(l2)
    return sum(abs(l1[i] - l2[i]) for i in range(len(l1)))


def part2(filename):
    l1, l2 = parse_input(filename)
    return sum(l1[i] * l2.count(l1[i]) for i in range(len(l1)))
