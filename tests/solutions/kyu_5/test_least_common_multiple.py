# pylint: disable=missing-docstring

"""Least Common Multiple"""

import pytest

from solutions.kyu_5 import lcm


EXAMPLES = (
    ('args', 'expected'),
    [
        ([2, 5], 10),
        ([2, 3, 4], 12),
        ([9], 9),
        ([0], 0),
        ([0, 1], 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert lcm(*args) == expected
