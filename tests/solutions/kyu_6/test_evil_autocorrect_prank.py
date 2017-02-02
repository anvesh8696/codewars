# pylint: disable=missing-docstring

"""Evil Autocorrect Prank"""

import pytest

from solutions.kyu_6 import autocorrect

EXAMPLES = (
    ('text', 'expected', 'comment'),
    [
        ('u', 'your sister', 'single "u"'),
        ('you', 'your sister', 'single "you"'),
        ('Youuuuu', 'your sister', 'capital case and a lot of uuu'),
        ('youtube', 'youtube', 'you included')
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text, expected, comment):
    assert autocorrect(text) == expected, comment
