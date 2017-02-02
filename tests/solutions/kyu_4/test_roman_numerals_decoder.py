# pylint: disable=missing-docstring

"""Roman Numerals Decoder"""

import pytest

from solutions.kyu_4.roman_numerals_decoder import solution


EXAMPLES = (
    ('roman', 'expected'),
    [
        ('I', 1),
        ('IV', 4),
        ('XXI', 21),
        ('MCMXC', 1990),
        ('MMVIII', 2008),
        ('MDCLXVI', 1666),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(roman, expected):
    assert solution(roman) == expected
