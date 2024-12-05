from .. import day4

test_input_1 = """
.XX...
.SAMXX
.AX.A.
XMAS.S
.X....
"""

test_input_2 = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

test_input_2_xmas_only = """
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
"""


def test_is_letter_involved_in_xmas():
    assert day4.is_x_in_xmas(input=test_input_1, coord=(0, 1))[0] is False
    assert day4.is_x_in_xmas(input=test_input_1, coord=(0, 2))[0] is True
    assert day4.is_x_in_xmas(input=test_input_1, coord=(1, 5))[0] is False
    assert day4.is_x_in_xmas(input=test_input_1, coord=(1, 4))[0] is True
    assert day4.is_x_in_xmas(input=test_input_1, coord=(2, 2))[0] is False

    assert day4.is_x_in_xmas(input=test_input_2, coord=(0, 4))[0] is True
    assert day4.is_x_in_xmas(input=test_input_2, coord=(0, 5))[0] is True
    assert day4.is_x_in_xmas(input=test_input_2, coord=(2, 2))[0] is False
    assert day4.is_x_in_xmas(input=test_input_2, coord=(9, 1)) == (True, 1)


def test_count_xmas():
    assert day4.count_xmas(test_input_1) == 4
    assert day4.count_xmas(test_input_2) == 18


def test_is_x_mas():
    assert day4.is_x_mas(test_input_2, (1, 2)) == (True, 1)
    assert day4.is_x_mas(test_input_2, (1, 2)) == (True, 1)
    assert day4.is_x_mas(test_input_2, (2, 6)) == (True, 1)
    assert day4.is_x_mas(test_input_2, (0, 7)) == (False, 0)


def test_count_x_mas():
    assert day4.count_x_mas(test_input_2) == 9
