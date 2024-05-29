#!/usr/bin/env python

import pytest

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


def test_mul_many_numbers() -> None:
    numbers = range(1, 10)
    calculator = SimpleCalculator()
    actual = calculator.mul(*numbers)
    expected = 362880
    assert actual == expected


def test_div_two_numbers_float() -> None:
    calculator = SimpleCalculator()
    actual = calculator.div(13, 2)
    expected = 6.5
    assert actual == expected


def test_dif_by_zero_returns_inf() -> None:
    calculator = SimpleCalculator()
    actual = calculator.div(5, 0)
    expected = float("inf")
    assert actual == expected


def test_mul_by_zero_raises_exception() -> None:
    calculator = SimpleCalculator()
    with pytest.raises(ValueError):
        calculator.mul(3, 0)


def test_avg_numbers() -> None:
    numbers = [2, 5, 12, 98]
    calculator = SimpleCalculator()
    actual = calculator.avg(numbers)
    expected = 29.25
    assert actual == expected


def test_avg_removes_upper_outliers() -> None:
    numbers = [2, 5, 12, 98]
    ut = 90
    numbers_under_ut = [2, 5, 12]
    calculator = SimpleCalculator()
    actual = calculator.avg(numbers, ut=ut)
    expected = calculator.avg(numbers_under_ut)
    assert actual == expected


def test_avg_removes_lower_outliers() -> None:
    numbers = [2, 5, 12, 98]
    lt = 10
    numbers_over_lt = [12, 98]
    calculator = SimpleCalculator()
    actual = calculator.avg(numbers, lt=lt)
    expected = calculator.avg(numbers_over_lt)
    assert actual == expected


def test_avg_includes_upper_threshold() -> None:
    numbers = [2, 5, 12, 98]
    ut = 12
    numbers_at_or_under_ut = [2, 5, 12]
    calculator = SimpleCalculator()
    actual = calculator.avg(numbers, ut=ut)
    expected = calculator.avg(numbers_at_or_under_ut)
    assert actual == expected


def test_avg_includes_lower_threshold() -> None:
    numbers = [2, 5, 12, 98]
    lt = 5
    numbers_at_or_above_lt = [5, 12, 98]
    calculator = SimpleCalculator()
    actual = calculator.avg(numbers, lt=lt)
    expected = calculator.avg(numbers_at_or_above_lt)
    assert actual == expected


def test_avg_empty_list() -> None:
    numbers = []
    calculator = SimpleCalculator()
    actual = calculator.avg(numbers)
    expected = 0
    assert actual == expected


def test_avg_empty_list_after_removing_outliers() -> None:
    numbers = [2, 5, 12, 98]
    lt = 15
    ut = 90
    calculator = SimpleCalculator()
    actual = calculator.avg(numbers, ut=ut, lt=lt)
    expected = 0
    assert actual == expected


def test_avg_removes_outliers_with_empty_list() -> None:
    numbers = []
    lt = 15
    ut = 90
    calculator = SimpleCalculator()
    actual = calculator.avg(numbers, ut=ut, lt=lt)
    expected = 0
    assert actual == expected


def test_avg_manages_zero_value_lower_threshold() -> None:
    numbers = [-1, 0, 1]
    lt = 0
    numbers_at_or_above_lt = [0, 1]
    calculator = SimpleCalculator()
    actual = calculator.avg(numbers, lt=lt)
    expected = calculator.avg(numbers_at_or_above_lt)
    assert actual == expected


def test_avg_manages_zero_value_upper_threshold() -> None:
    numbers = [-1, 0, 1]
    ut = 0
    numbers_at_or_below_ut = [-1, 0]
    calculator = SimpleCalculator()
    actual = calculator.avg(numbers, ut=ut)
    expected = calculator.avg(numbers_at_or_below_ut)
    assert actual == expected


def test_avg_accepts_generators() -> None:
    gen_numbers = (n for n in [2, 5, 12, 98])
    calculator = SimpleCalculator()
    actual = calculator.avg(gen_numbers)
    expected = 29.25
    assert actual == expected
