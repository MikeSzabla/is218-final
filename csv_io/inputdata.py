"""InputData.py: stores the InputData class"""

import os
from pathlib import Path
import pandas as pd


class InputData:
    """InputData class: Responsible for building and returning dataframes using files inside a passed in directory"""

    input_dir = ""
    list_of_input_paths = []
    input_dataframe = pd.DataFrame(data={'value_a': [], 'value_b': [], 'operation': [], 'input_file': [], 'record_number': []})

    def __init__(self, input_dir):
        """Initial constructor that sets variables and generates """
        InputData.input_dir = input_dir
        InputData.set_list_of_input_paths(InputData.generate_list_of_input_paths(input_dir))
        InputData.populate_dataframe(InputData.get_list_of_input_paths())

    @staticmethod
    def generate_list_of_input_paths(folder_dir):
        """takes all files in the passed in directory and returns a list of their paths"""
        path_list = []
        for root, dirs, files in os.walk(folder_dir):
            for file in files:
                if Path(file).suffix != '.csv':  # pragma: no cover
                    continue
                path_list.append(os.path.abspath(os.path.join(root, file)))
        return path_list

    @staticmethod
    def get_list_of_input_paths():
        """return list of input paths"""
        return InputData.list_of_input_paths

    @staticmethod
    def set_list_of_input_paths(path_list):
        """set the list of file paths to be equal to the passed in list"""
        InputData.list_of_input_paths = path_list

    @staticmethod
    def populate_dataframe(list_of_input_paths):
        """"populate the dataframe with data from the files passed in through a list"""
        for path in list_of_input_paths:
            dataframe_from_csv = pd.read_csv(path)
            path_col = [os.path.relpath(path, InputData.input_dir)] * len(dataframe_from_csv.index)  # add column of file paths
            record_num_col = list(range(1, len(dataframe_from_csv.index)+1))
            dataframe_from_csv['input_file'] = path_col
            dataframe_from_csv['record_number'] = record_num_col
            InputData.append_dataframe(dataframe_from_csv)

    @staticmethod
    def append_dataframe(df):
        """takes the passed in dataframe and adds it the the bottom of the main input_dataframe"""
        InputData.input_dataframe = pd.concat([InputData.get_input_dataframe(), df], ignore_index=True)

    @staticmethod
    def get_input_dataframe():
        """returns the input_dataframe"""
        return InputData.input_dataframe

    @staticmethod
    def clear_input_dataframe():
        """clears the input_dataframe"""
        InputData.input_dataframe.drop(InputData.input_dataframe.index, inplace=True)
