"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


@pytest.fixture(name="calculator_fixture")
def fixture_calculator_fixture():
    """method that will run each time it's passed into a test"""
    Calculator.clear_history()
    Calculator.add_number((1, 2, 3))  # result = 6
    Calculator.subtract_number((3, 2, 1))  # result = 0
    Calculator.multiply_number((2, 2, 2))  # result = 8
    Calculator.divide_number((8, 2, 2))  # result = 2


def test_get_history_length(calculator_fixture):  # pylint: disable=unused-argument
    """tests the the getter for history length"""
    assert Calculator.get_history_length() == 4


def test_calculator_history(calculator_fixture):  # pylint: disable=unused-argument
    """tests history by checking length after adding operation"""

    Calculator.add_number((1,))
    assert Calculator.get_history_length() == 5


def test_get_last_calc_result(calculator_fixture):  # pylint: disable=unused-argument
    """tests the get_result_of_last_calculation method"""
    assert Calculator.get_result_of_last_calculation() == float(2)


def test_get_last_operation(calculator_fixture):  # pylint: disable=unused-argument
    """tests the get_last_operation method in Calculator"""
    last_operation = Calculator.get_last_operation()
    assert isinstance(last_operation, Division)
    assert last_operation.get_result() == float(2)


def test_get_first_calc_result(calculator_fixture):  # pylint: disable=unused-argument
    """tests the get_result_of_first_calculation method"""
    assert Calculator.get_result_of_first_calculation() == float(6)


def test_get_first_operation(calculator_fixture):  # pylint: disable=unused-argument
    """tests the get_first_operation method in Calculator"""
    first_operation = Calculator.get_first_operation()
    assert isinstance(first_operation, Addition)
    assert first_operation.get_result() == float(6)


def test_clear_history():
    """tests the clear history method in Calculator"""
    Calculator.clear_history()
    assert Calculator.get_history_length() == 0


def test_remove_from_history(calculator_fixture):  # pylint: disable=unused-argument
    """tests the remove_from_history method in Calculator"""
    removed_operation = Calculator.remove_from_history(1)
    assert isinstance(removed_operation, Subtraction)
    assert removed_operation.get_result() == float(0)
    assert Calculator.get_history_length() == 3


def test_calculator_add_static():
    """Testing the add function of the calculator"""
    Calculator.add_number((1, 1))
    last_operation = Calculator.get_last_operation()
    assert isinstance(last_operation, Addition)


def test_calculator_subtract_static():
    """Testing the subtract method of the calculator"""
    Calculator.subtract_number((1, 1))
    last_operation = Calculator.get_last_operation()
    assert isinstance(last_operation, Subtraction)


def test_calculator_multiply_static():
    """Testing the multiply method of the calculator"""
    Calculator.multiply_number((1, 1))
    last_operation = Calculator.get_last_operation()
    assert isinstance(last_operation, Multiplication)


def test_calculator_divide_static():
    """Testing the divide method of the calculator"""
    Calculator.divide_number((1, 1))
    last_operation = Calculator.get_last_operation()
    assert isinstance(last_operation, Division)
