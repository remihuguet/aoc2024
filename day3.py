import re


def extract_muls_and_dos(intput: str) -> list[str]:
    pattern = re.compile(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))")
    return pattern.findall(intput)


def extract_muls(input: str) -> list[int]:
    muls_and_dos = extract_muls_and_dos(input)
    enabled = True
    muls = []
    for item in muls_and_dos:
        if item == "do()":
            enabled = True
        elif item == "don't()":
            enabled = False
        elif enabled:
            n, m = re.findall(r"\d{1,3}", item)
            muls.append((int(n), int(m)))

    return muls


def score(input: str) -> int:
    return sum(n * m for n, m in extract_muls(input))
