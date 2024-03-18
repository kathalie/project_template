import os.path
import pandas as pd


def read_from_console(prompt):
    """
    Reads a user console input using a standard function.

    Args:
        prompt (str): Used to tell a user what input is expected.

    Returns: str. User input.
    """
    return input(prompt)


def read_from_file(filepath):
    """
    Reads a file content by a given name.

    Args:
        filepath (str): The path to the file to read from.

    Returns:
        str. Contents of the requested file.
        None. If there is no such file or directory.
    """
    if not os.path.isfile(filepath):
        print(f'Not found: {filepath}')
        return None

    with open(filepath) as file:
        return file.read()


def read_from_file_using_pandas(filepath):
    """
    Reads comma-separated values from a .csv file using pandas.

    Args:
        filepath (str): A path to a .csv file to read from.

    Returns: DataFrame. Contents of the requested .csv file converted to a
    pandas.DataFrame.
    """
    if not os.path.isfile(filepath):
        print(f'Not found: {filepath}')
        return None

    return pd.read_csv(filepath)
