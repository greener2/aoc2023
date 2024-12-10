"""Advent of Code: 2023 - Day 01."""

from __future__ import annotations

import re

from . import utils

EXAMPLE = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip()

matcher = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")

number_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def read_data(data: list[str] | None = None) -> list[str]:
    """Read the data."""
    return data or utils.read_example(EXAMPLE)


def solve(data: list[str] | None = None) -> tuple[int, int]:
    """
    Solve the problem.

    You can write docstests here too:

    >>> solve()
    (0, 0)
    """
    data = read_data(data=data)

    calibration_sum = 0
    alphanum_cal_sum = 0
    for line in data:
        digits_only = "".join([d for d in line if d.isdigit()])

        if len(digits_only) == 0:
            calibration_sum += 0
        elif len(digits_only) == 1:
            calibration_sum += int("".join((digits_only, digits_only)))
        else:
            calibration_sum += int("".join((digits_only[0], digits_only[-1])))

        m = matcher.findall(line)

        first_digit = m[0]
        last_digit = m[-1]
        if first_digit in number_map:
            first_digit = number_map[first_digit]
        if last_digit in number_map:
            last_digit = number_map[last_digit]

        alphanum_cal_sum += 10 * int(first_digit) + int(last_digit)

    p1, p2 = calibration_sum, alphanum_cal_sum
    return p1, p2


def test_solve() -> None:
    assert solve() == (0, 0)
