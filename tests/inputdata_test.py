import pytest
import pandas as pd
from pathlib import Path
from csv_io.inputdata import InputData


@pytest.fixture
def io_test_dir():
    """returns the io_tests dir"""
    return Path(__file__).parent / 'io_tests'


@pytest.fixture
def correct_input_dataframe():
    correct_input_dataframe = pd.DataFrame({'value_a': [1.0], 'value_b': [1.0],
                                            'operation': ['subtraction'],
                                            'input_file': ['input_test.csv'],
                                            'record_number': [1.0]})
    return correct_input_dataframe


@pytest.fixture
def input_data_setup(io_test_dir):
    """initializes InputData to trigger the constructor and fill it with input data"""
    # create a dataframe using the input data
    InputData.clear_input_dataframe()
    InputData(io_test_dir)


def test_get_list_of_input_paths(io_test_dir, input_data_setup):
    """tests the get_list_of_input_paths method"""
    assert InputData.get_list_of_input_paths() == [str(io_test_dir / 'input_test.csv')]


def test_generate_list_of_input_paths(io_test_dir):
    """tests the generate_list_of_input_paths method"""
    assert InputData.generate_list_of_input_paths(io_test_dir) == [str(io_test_dir / 'input_test.csv')]


def test_set_list_of_input_paths(input_data_setup):
    """tests the set_list_of_input_paths method"""
    InputData.set_list_of_input_paths(['something else'])
    assert InputData.get_list_of_input_paths() == ['something else']


def test_get_input_dataframe(input_data_setup):
    """tests the get_input_dataframe method"""
    df = InputData.get_input_dataframe()
    assert isinstance(df, pd.core.frame.DataFrame)


def test_append_dataframe(input_data_setup, correct_input_dataframe):
    """tests the append_dataframe method"""
    InputData.append_dataframe(correct_input_dataframe)
    assert InputData.get_input_dataframe().equals(pd.concat([correct_input_dataframe, correct_input_dataframe],
                                                            ignore_index=True))


def test_populate_dataframe(input_data_setup, correct_input_dataframe):
    """tests the populate_dataframe method"""
    # populate_dataframe is called in the constructor so the results are being testing
    assert InputData.get_input_dataframe().equals(correct_input_dataframe)
