"""Test of the Division operation"""
import pytest
from calc.operations.division import Division


def test_division():
    """method calling Division operation"""
    # Arrange
    division = Division.create((8, 2, 2))
    # Act
    result = division.get_result()
    # Assert
    assert result == 2

    # Arrange
    division = Division.create((8, 2, 0))
    # Assert
    with pytest.raises(ZeroDivisionError):
        # Act
        result = division.get_result()
