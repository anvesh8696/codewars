# coding=utf-8
# pylint: disable=missing-docstring

"""
What's wrong with these identifiers? tests
"""

import pytest

from solutions.kyu_8 import Person


def test_person_is_defined():
    try:
        Person
    except NameError:
        pytest.fail('Person object is not defined')


def test_person_has_4_properties():
    assert len(Person.keys()) == 4
