import pytest

from calc import add, mean


def test_add():
    assert add(2, 3) == 5


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5


def test_mean_of_nothing_is_an_error():
    with pytest.raises(ValueError):
        mean([])
