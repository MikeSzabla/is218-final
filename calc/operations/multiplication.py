"""Multiplication Operation"""
from calc.operations.calculation import Calculation


class Multiplication(Calculation):  # pylint: disable=too-few-public-methods
    """Multiplication Class"""

    def get_result(self):
        """returns value_a multiplied by value_b"""
        result = self.values[0]
        for value in self.values[1:]:
            result *= value
        return result
