from .. import day3

test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test_input_2 = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)


def test_extract_muls():
    assert day3.extract_muls(test_input) == [
        (2, 4),
        (5, 5),
        (11, 8),
        (8, 5),
    ]


def test_extract_muls_and_dos():
    assert day3.extract_muls_and_dos(test_input_2) == [
        "mul(2,4)",
        "don't()",
        "mul(5,5)",
        "mul(11,8)",
        "do()",
        "mul(8,5)",
    ]


def test_extract_muls_part_2():
    assert day3.extract_muls(test_input_2) == [
        (2, 4),
        (8, 5),
    ]


def test_part1():
    assert day3.score(test_input) == 161


def test_part2():
    assert day3.score(test_input_2) == 48
