from .. import day1


def test_parse_day1_input():
    expected = ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
    assert day1.parse_input("inputs/day1_test.txt") == expected


def test_day_1_part_1():
    expected = 11
    assert day1.part1("inputs/day1_test.txt") == expected


def test_day_1_part_2():
    expected = 31
    assert day1.part2("inputs/day1_test.txt") == expected
