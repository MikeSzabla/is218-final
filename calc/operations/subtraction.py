"""Subtraction Operation"""
from calc.operations.calculation import Calculation


class Subtraction(Calculation):  # pylint: disable=too-few-public-methods
    """Subtraction Class"""

    def get_result(self):
        """returns value_a subtract value_b"""
        result = self.values[0]
        for value in self.values[1:]:
            result -= value
        return result
