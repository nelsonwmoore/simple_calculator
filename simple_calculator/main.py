"""Main module for the simple_calculator package."""

import operator
from functools import reduce


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
        return reduce(operator.mul, args)
