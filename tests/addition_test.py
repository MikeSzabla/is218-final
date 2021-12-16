"""Test of the Addition operation"""
from calc.operations.addition import Addition
from pathlib import Path
import pandas as pd

THIS_DIR = Path(__file__).parent
data_path = THIS_DIR / 'csv_tests/addition_test_small.csv'


def test_addition():
    """method calling Addition operation"""
    dataframe = pd.read_csv(data_path)
    for index, row in dataframe.iterrows():
        # Arrange & Act
        addition = Addition.create((row['value a'], row['value b']))
        result = addition.get_result()
        # Assert
        assert result == float(row['answer'])
