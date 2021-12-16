"""outputdata_test.py: contains all tests for methods in outputdata.py"""
import pytest
import pandas as pd
from pathlib import Path
from csv_io.inputdata import InputData
from csv_io.outputdata import OutputData


@pytest.fixture
def io_test_dir():
    """returns the io_tests dir"""
    return Path(__file__).parent / 'io_tests'


@pytest.fixture
def input_data_setup(io_test_dir):
    """initializes InputData to trigger the constructor and fill it with input data"""
    # create a dataframe using the input data
    InputData.clear_input_dataframe()
    InputData(io_test_dir)


@pytest.fixture
def export_data_setup(input_data_setup):
    """initializes the OutputData class with the input dataframe created in input_setup"""
    OutputData.set_output_data([])
    OutputData(InputData.get_input_dataframe())


def test_set_output_data():
    """tests the set_output_data method"""
    OutputData.set_output_data(['Something Else'])
    assert OutputData.get_output_data() == ['Something Else']


def test_set_exception_data():
    """tests the set_exception_data method"""
    OutputData.set_exception_data(['Something Else'])
    assert OutputData.get_exception_data() == ['Something Else']


def test_get_output_data():
    """tests the get_output_data method"""
    OutputData.output_data = ['Something Else']
    assert OutputData.get_output_data() == ['Something Else']


def test_get_exception_data():
    """tests the get_exception_data method"""
    OutputData.exception_data = ['Something Else']
    assert OutputData.get_exception_data() == ['Something Else']


def test_generate_exception_dataframe():
    test_data = [{'col1': [1], 'col2':[2]}]
    OutputData.set_exception_data(test_data)
    assert OutputData.generate_exception_dataframe().equals(pd.DataFrame.from_dict(test_data))


def test_append_output_data():
    """tests the append_output_data method"""
    test_data = [{'col1': [1], 'col2': [2]}]
    OutputData.set_output_data(test_data)
    OutputData.append_output_data(test_data[0])
    test_data.append(test_data[0])
    assert OutputData.get_output_data() == test_data


def test_append_exception_data():
    """tests the exception_output_data method"""
    test_data = [{'col1': [1], 'col2': [2]}]
    OutputData.set_exception_data(test_data)
    OutputData.append_exception_data(test_data[0])
    test_data.append(test_data[0])
    assert OutputData.get_exception_data() == test_data


def test_get_calc_result():
    """tests the get_calc_result method"""
    assert OutputData.get_calc_result(1, 1, 'addition') == 2
    assert OutputData.get_calc_result(1, 1, 'subtraction') == 0
    assert OutputData.get_calc_result(1, 1, 'multiplication') == 1.0
    assert OutputData.get_calc_result(1, 1, 'division') == 1.0
    with pytest.raises(ZeroDivisionError):
        OutputData.get_calc_result(1, 0, 'division')
