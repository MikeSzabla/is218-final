""" main.py: holds the Calculator class definition"""
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


class Calculator:
    """ This is the Calculator class"""

    history = []

    @staticmethod
    def get_history():
        """returns the history list storing past operations"""
        return Calculator.history

    @staticmethod
    def add_calculation_to_history(calculation):
        """adds a calculation to the end of the history"""
        Calculator.history.append(calculation)

    @staticmethod
    def get_result_of_last_calculation():
        """returns the results of the last item in the calculator history"""
        return Calculator.get_history()[-1].get_result()

    @staticmethod
    def get_last_operation():
        """grabs the latest operation from the history"""
        return Calculator.get_history()[-1]

    @staticmethod
    def get_result_of_first_calculation():
        """returns the results of the first item in the calculator history"""
        return Calculator.get_history()[0].get_result()

    @staticmethod
    def get_first_operation():
        """grabs the first operation from the history"""
        return Calculator.get_history()[0]

    @staticmethod
    def get_history_length():
        """gets the length of the calculator history"""
        return len(Calculator.get_history())

    @staticmethod
    def clear_history():
        """clears the calculator history"""
        Calculator.history = []

    @staticmethod
    def remove_from_history(index):
        """remove an item from the calculator's history via index"""
        return Calculator.history.pop(index)

    @staticmethod
    def add_number(*args):
        """adds all passed in args and adds operation to history"""
        Calculator.add_calculation_to_history(Addition.create(*args))

    @staticmethod
    def subtract_number(*args):
        """subtracts from first value all subsequent values"""
        Calculator.add_calculation_to_history(Subtraction.create(*args))

    @staticmethod
    def multiply_number(*args):
        """multiplies all passed values"""
        Calculator.add_calculation_to_history(Multiplication.create(*args))

    @staticmethod
    def divide_number(*args):
        """divides first passed value by all subsequent values"""
        Calculator.add_calculation_to_history(Division.create(*args))
