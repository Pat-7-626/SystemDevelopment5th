"""
A simple calculator module with basic arithmetic operations.
"""

MAX_VALUE = 1000000
MIN_VALUE = -1000000


class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""


class Calculator:
    """Calculator class providing basic arithmetic operations."""

    def _validate_input(self, *values):
        """Validate that inputs are within the allowed range."""
        for v in values:
            if not (MIN_VALUE <= v <= MAX_VALUE):
                raise InvalidInputException(
                    f"Input {v} is out of valid range: {MIN_VALUE} to {MAX_VALUE}."
                )

    def add(self, a, b):
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_input(a, b)
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_input(a, b)
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_input(a, b)
        return a * b

    def divide(self, a, b):
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
            ValueError: If b is zero
        """
        self._validate_input(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
