from collections import defaultdict


def parse_input(filename: str) -> tuple[dict, list[list]]:
    rules = defaultdict(list)
    updates = []
    with open(filename, "r") as f:
        for line in f:
            if "|" in line:
                n1, n2 = map(int, line.strip().split("|"))
                rules[n1].append(n2)
            elif "," in line:
                updates.append(list(map(int, line.strip().split(","))))
    return rules, updates


def update_is_correct(rules: dict, update: list[int]) -> bool:
    for i, number in enumerate(update[1:]):
        if any([n in rules[number] for n in update[: i + 1]]):
            return False
    return True


def reorder_update(rules: dict, update: list[int]) -> list[int]:
    ordered = []
    for i, n in enumerate(update):
        n_index = 0
        for j, m in enumerate(ordered):
            if n in rules[m]:
                n_index = j + 1
        ordered.insert(n_index, n)
    return ordered


def part1(filename):
    rules, updates = parse_input(filename)
    correct_rules = [update for update in updates if update_is_correct(rules, update)]
    return sum(update[len(update) // 2] for update in correct_rules)


def part2(filename):
    rules, updates = parse_input(filename)
    uncorrect_rules = [
        reorder_update(rules, update)
        for update in updates
        if not update_is_correct(rules, update)
    ]
    return sum(update[len(update) // 2] for update in uncorrect_rules)
