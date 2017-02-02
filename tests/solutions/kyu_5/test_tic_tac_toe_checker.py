# pylint: disable=missing-docstring

"""Tic-Tac-Toe Checker"""

import pytest

from solutions.kyu_5 import isSolved

EXAMPLES = (
    ('board', 'expected'),
    [
        ([[0, 0, 1], [0, 1, 2], [2, 1, 0]], -1),
        ([[1, 1, 1], [0, 0, 0], [0, 0, 0]], 1),
        ([[2, 2, 2], [0, 0, 0], [0, 0, 0]], 2),
        ([[1, 2, 0], [0, 1, 2], [0, 0, 1]], 1),
        ([[2, 1, 2], [2, 1, 1], [1, 2, 1]], 0)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(board, expected):
    assert isSolved(board) == expected
