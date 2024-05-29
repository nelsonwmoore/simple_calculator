"""Main module for the simple_calculator package."""

from __future__ import annotations

import operator
from functools import reduce
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


class SimpleCalculator:
    """A simple calculator class."""

    def add(self, *args: int) -> int:
        """Add numbers."""
        return sum(args)

    def sub(self, a: int, b: int) -> int:
        """Subtract b from a."""
        return a - b

    def mul(self, *args: int) -> int:
        """Multiply numbers."""
        if not all(args):
            raise ValueError
        return reduce(operator.mul, args)

    def div(self, a: int, b: int) -> float:
        """Divide a (dividend) by b (divisor)."""
        try:
            return a / b
        except ZeroDivisionError:
            return float("inf")

    def avg(
        self,
        nums: Iterable[int | float],
        ut: int | None = None,
        lt: int | None = None,
    ) -> float:
        """Calculate the average of numbers."""
        count = 0
        total = 0

        for num in nums:
            if ut is not None and num > ut:
                continue
            if lt is not None and num < lt:
                continue
            count += 1
            total += num

        if count == 0:
            return 0

        return total / count
