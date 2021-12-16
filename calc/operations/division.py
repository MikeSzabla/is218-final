"""Division Operation"""
from calc.operations.calculation import Calculation


class Division(Calculation):  # pylint: disable=too-few-public-methods
    """Division Class"""

    def get_result(self):
        """returns value_a divided by value_b"""
        result = self.values[0]
        for value in self.values[1:]:
            result = result / value
        return result
