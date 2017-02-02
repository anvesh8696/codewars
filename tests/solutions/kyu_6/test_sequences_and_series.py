# pylint: disable=missing-docstring

"""Sequences and Series"""

import pytest

from solutions.kyu_6 import get_score

EXAMPLES = (
    ('num', 'expected'),
    [
        (1, 50),
        (2, 150),
        (3, 300),
        (4, 500),
        (5, 750),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(num, expected):
    assert get_score(num) == expected
