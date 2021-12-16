"""Test of the Multiplication operation"""
from calc.operations.multiplication import Multiplication


def test_multiplication():
    """method calling Multiplication operation"""
    # Arrange
    multiplication = Multiplication.create((2, 3, 4))
    # Act
    result = multiplication.get_result()
    # Assert
    assert result == float(24)
