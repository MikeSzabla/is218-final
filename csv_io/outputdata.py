import os
import pandas as pd
import time
from calc.calculator import Calculator


class OutputData:
    calculator = Calculator()
    output_data = []
    exception_data = []

    def __init__(self, input_dataframe):
        OutputData.set_output_data([])
        OutputData.populate_output_data(input_dataframe)

    @staticmethod
    def get_output_data():
        return OutputData.output_data

    @staticmethod
    def get_exception_data():
        return OutputData.exception_data

    @staticmethod
    def get_time():
        return int(time.time())

    @staticmethod
    def generate_exception_dataframe():
        exception_dataframe = pd.DataFrame.from_dict(OutputData.get_exception_data())
        return exception_dataframe

    @staticmethod
    def generate_output_dataframe():
        output_dataframe = pd.DataFrame.from_dict(OutputData.get_output_data())
        return output_dataframe

    @staticmethod
    def populate_output_data(input_df):
        for index in input_df.index:  # pragma: no cover
            try:
                OutputData.append_output_data({'time': OutputData.get_time(),
                                               'input_file': input_df.iloc[index]['input_file'],
                                               'record_number': input_df.iloc[index]['record_number'],
                                               'value_a': input_df.iloc[index]['value_a'],
                                               'value_b': input_df.iloc[index]['value_b'],
                                               'operation': input_df.iloc[index]['operation'],
                                               'result': OutputData.get_calc_result(input_df.iloc[index]['value_a'],
                                                                                    input_df.iloc[index]['value_b'],
                                                                                    input_df.iloc[index]['operation'])})
            except ZeroDivisionError:
                OutputData.append_exception_data({'record_number': input_df.iloc[index]['record_number'],
                                                  'input_file': input_df.iloc[index]['input_file'],
                                                  'value_a': input_df.iloc[index]['value_a'],
                                                  'value_b': input_df.iloc[index]['value_b'],
                                                  'operation': input_df.iloc[index]['operation'],
                                                  'error': 'ZeroDivisionError'})

    @staticmethod
    def append_output_data(row):
        OutputData.output_data.append(row)

    @staticmethod
    def append_exception_data(row):
        OutputData.exception_data.append(row)

    @staticmethod
    def set_output_data(data_list):
        OutputData.output_data = data_list

    @staticmethod
    def set_exception_data(data_list):
        OutputData.exception_data = data_list

    @staticmethod
    def get_calc_result(value_a, value_b, operation):
        if operation == "addition":
            OutputData.calculator.add_number((value_a, value_b))
            return OutputData.calculator.get_result_of_last_calculation()
        elif operation == "subtraction":
            OutputData.calculator.subtract_number((value_a, value_b))
            return OutputData.calculator.get_result_of_last_calculation()
        elif operation == "multiplication":
            OutputData.calculator.multiply_number((value_a, value_b))
            return OutputData.calculator.get_result_of_last_calculation()
        elif operation == "division":
            OutputData.calculator.divide_number((value_a, value_b))
            return OutputData.calculator.get_result_of_last_calculation()
