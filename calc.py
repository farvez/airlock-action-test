"""A tiny module for the tests to check."""


def add(a, b):
    return a + b


def mean(values):
    if not values:
        raise ValueError("mean() of an empty list")
    return sum(values) / len(values)
