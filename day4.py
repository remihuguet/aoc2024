DELTA_CANDIDATES = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]


def is_x_in_xmas(input: str, coord: tuple[int, int]) -> bool:
    input_array = [list(row) for row in input.strip().split("\n")]
    n, m = coord
    letter = input_array[n][m]
    if letter != "X":
        return False, 0
    count = 8
    for delta_i, delta_j in DELTA_CANDIDATES:
        for i, next_letter in enumerate("MAS"):
            coord = (n + (i + 1) * delta_i, m + (i + 1) * delta_j)
            if (
                coord[0] < 0
                or coord[1] < 0
                or coord[0] >= len(input_array)
                or coord[1] >= len(input_array[0])
            ):
                count -= 1
                break
            if input_array[n + (i + 1) * delta_i][m + (i + 1) * delta_j] != next_letter:
                count -= 1
                break
    return count > 0, count


def count_xmas(input: str) -> int:
    input_array = [list(row) for row in input.strip().split("\n")]
    total = 0
    for i, row in enumerate(input_array):
        for j, letter in enumerate(row):
            if letter == "X":
                is_in_x, count = is_x_in_xmas(input, (i, j))
                if is_in_x:
                    total += count
    return total


X_MAS_POSITIONS = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
X_MAS_COMBI = [
    ("M", "S", "M", "S"),
    ("S", "S", "M", "M"),
    ("M", "M", "S", "S"),
    ("S", "M", "S", "M"),
]


def is_x_mas(input: str, coord: tuple[int, int]) -> tuple[bool, int]:
    input_array = [list(row) for row in input.strip().split("\n")]
    n, m = coord
    letter = input_array[n][m]
    if letter != "A":
        return False, 0
    try:
        cross_letters = tuple(input_array[n + i][m + j] for i, j in X_MAS_POSITIONS)
    except IndexError:
        return False, 0
    if cross_letters in X_MAS_COMBI:
        return True, 1
    return False, 0


# This does not work on the real input, I had a +1 offset on the final count :shrug:
def count_x_mas(input):
    input_array = [list(row) for row in input.strip().split("\n")]
    total = 0
    for i, row in enumerate(input_array):
        for j, _ in enumerate(row):
            total += is_x_mas(input, (i, j))[1]
    return total
