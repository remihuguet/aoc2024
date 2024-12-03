def parse_input(filename):
    with open(filename) as f:
        return [[int(x) for x in line.split()] for line in f]


def is_report_safe(report):
    diffs = [r - report[i + 1] for i, r in enumerate(report[:-1])]
    return all([abs(d) < 4 and d != 0 for d in diffs]) and (
        all([d >= 0 for d in diffs]) or all([d <= 0 for d in diffs])
    )


def is_report_safe_problem_dampener(report):
    if is_report_safe(report):
        return True
    else:
        for i, r in enumerate(report):
            alt = report.copy()
            alt.pop(i)
            if is_report_safe(alt):
                return True
    return False


def part1(filename):
    return sum([is_report_safe(report) for report in parse_input(filename)])


def part2(filename):
    return sum(
        [is_report_safe_problem_dampener(report) for report in parse_input(filename)]
    )
