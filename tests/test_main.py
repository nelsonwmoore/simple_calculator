#!/usr/bin/env python

from simple_calculator.main import SimpleCalculator


def test_add_two_numbers() -> None:
    calculator = SimpleCalculator()
    actual = calculator.add(4, 5)
    expected = 9
    assert actual == expected


def test_add_three_numbers() -> None:
    calculator = SimpleCalculator()
    actual = calculator.add(4, 5, 6)
    expected = 15
    assert actual == expected


def test_add_many_numbers() -> None:
    numbers = range(100)
    calculator = SimpleCalculator()
    actual = calculator.add(*numbers)
    expected = 4950
    assert actual == expected


def test_sub_two_numbers() -> None:
    calculator = SimpleCalculator()
    actual = calculator.sub(10, 3)
    expected = 7
    assert actual == expected


def test_mul_two_numbers() -> None:
    calculator = SimpleCalculator()
    actual = calculator.mul(4, 5)
    expected = 20
    assert actual == expected


def test_mul_many_numers() -> None:
    numbers = range(1, 10)
    calculator = SimpleCalculator()
    actual = calculator.mul(*numbers)
    expected = 362880
    assert actual == expected
