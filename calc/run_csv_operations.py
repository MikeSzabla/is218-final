from pathlib import Path
from csv_io.inputdata import InputData
from csv_io.outputdata import OutputData
import os
import shutil
# import datetime


def run_operations():
    # gather necessary directory paths
    root_dir = Path(__file__).parent.parent
    input_folder_dir = root_dir / 'input'
    output_folder_dir = root_dir / 'output'
    done_folder_dir = root_dir / 'done'
    # now = datetime.datetime.now()

    # create a dataframe using the input data
    input_data = InputData(input_folder_dir)
    input_dataframe = input_data.get_input_dataframe()

    # create a dataframe with the info that will be output
    output_data = OutputData(input_dataframe)
    output_dataframe = output_data.generate_output_dataframe()
    exception_dataframe = output_data.generate_exception_dataframe()

    # append result CSVs from output_dataframe and exception_dataframe
    if not output_dataframe.empty:
        filename = os.path.join(output_folder_dir, 'calculation_results')
        if not os.path.isfile(filename):
            output_dataframe.to_csv(filename)
        else:  # else it exists so append without writing the header
            output_dataframe.to_csv(filename, mode='a', header=False)

    if not exception_dataframe.empty:
        if not exception_dataframe.empty:
            filename = os.path.join(output_folder_dir, 'exceptions')
            if not os.path.isfile(filename):
                exception_dataframe.to_csv(filename)
            else:  # else it exists so append without writing the header
                exception_dataframe.to_csv(filename, mode='a', header=False)

    # move files to done directory
    for file in input_data.get_list_of_input_paths():
        shutil.move(file, done_folder_dir)


if __name__ == '__main__':
    run_operations()
