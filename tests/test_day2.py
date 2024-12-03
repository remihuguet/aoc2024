import pytest

from .. import day2


def test_parse_input():
    expected = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert day2.parse_input("inputs/day2_test.txt") == expected


@pytest.mark.parametrize(
    ("report", "expected"),
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_day2_is_report_safe(report, expected):
    assert day2.is_report_safe(report) is expected


def test_day_2_part_1():
    expected = 2
    assert day2.part1("inputs/day2_test.txt") == expected


@pytest.mark.parametrize(
    ("report", "expected"),
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], True),
        ([8, 6, 4, 4, 1], True),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_day2_is_report_safe_problem_dampener(report, expected):
    assert day2.is_report_safe_problem_dampener(report) is expected


def test_day_2_part_2():
    expected = 4
    assert day2.part2("inputs/day2_test.txt") == expected
