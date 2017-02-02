# pylint: disable=missing-docstring

"""Title Case"""

import pytest

from solutions.kyu_6 import title_case

EXAMPLES = (
    ('title', 'minor', 'result'),
    [
        ('a clash of KINGS', 'a an the of', 'A Clash of Kings'),
        ('THE WIND IN THE WILLOWS', 'The In', 'The Wind in the Willows')
    ]
)


def test_empty_string():
    assert title_case('') == ''


@pytest.mark.parametrize(*EXAMPLES)
def test_lowercase(title, minor, result):
    assert title_case(title, minor) == result


def test_without_second_argument():
    assert title_case('the quick brown fox') == 'The Quick Brown Fox'
