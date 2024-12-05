from .. import day5


def test_parse_input():
    rules, updates = (
        {
            47: [53, 13, 61, 29],
            97: [13, 61, 47, 29, 53, 75],
            75: [29, 53, 47, 61, 13],
            61: [13, 53, 29],
            29: [13],
            53: [29, 13],
        },
        [
            [75, 47, 61, 53, 29],
            [97, 61, 53, 29, 13],
            [75, 29, 13],
            [75, 97, 47, 61, 53],
            [61, 13, 29],
            [97, 13, 75, 29, 47],
        ],
    )
    assert day5.parse_input("inputs/day5_test.txt") == (rules, updates)


def test_update_is_correct():
    rules, updates = day5.parse_input("inputs/day5_test.txt")

    assert day5.update_is_correct(rules, updates[0]) is True
    assert day5.update_is_correct(rules, updates[1]) is True
    assert day5.update_is_correct(rules, updates[2]) is True
    assert day5.update_is_correct(rules, updates[3]) is False
    assert day5.update_is_correct(rules, updates[4]) is False
    assert day5.update_is_correct(rules, updates[5]) is False


def test_part1():
    assert day5.part1("inputs/day5_test.txt") == 143


def test_reorder_update():
    rules, updates = day5.parse_input("inputs/day5_test.txt")

    assert day5.reorder_update(rules, updates[4]) == [61, 29, 13]
    assert day5.reorder_update(rules, updates[3]) == [97, 75, 47, 61, 53]
    assert day5.reorder_update(rules, updates[5]) == [97, 75, 47, 29, 13]


def test_part2():
    assert day5.part2("inputs/day5_test.txt") == 123
