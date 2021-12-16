"""Calculation"""


class Calculation:  # pylint: disable=too-few-public-methods
    """Operation Class"""
    def __init__(self, args: tuple):
        """default constructor setting up value variables"""
        self.values = Calculation.args_to_float_tuple(args)

    @classmethod
    def create(cls, args: tuple):
        """factory method to create operation objects"""
        return cls(args)

    @staticmethod
    def args_to_float_tuple(input_tuple):
        """converts each item in input_tuple to a float; return new tuple"""
        float_args = []
        for arg in input_tuple:
            float_args.append(float(arg))
        return tuple(float_args)
