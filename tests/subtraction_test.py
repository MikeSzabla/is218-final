"""Test of the Subtraction operation"""
from calc.operations.subtraction import Subtraction


def test_subtraction():
    """method calling Addition operation"""
    # Arrange
    subtraction = Subtraction.create((1, 2, 3))
    # Act
    result = subtraction.get_result()
    # Assert
    assert result == float(-4)
