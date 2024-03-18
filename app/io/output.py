import pandas as pd


def write_to_console(text):
    """
    Writes to console a given text using standard function.

    Args:
        text (str): The text to be printed in console.
    """
    print(text)


def write_to_file(contents, filepath):
    """
    Writes contents to a file by its path.

    Note: if a file by filepath already exists, it will be overwritten!

    Args:
        contents (str): Text to be writen to a file.
        filepath (str): A path to a file
    """
    if not isinstance(contents, str):
        print(f'Failed to write {contents}, because it is not of type str!')
        return

    with open(filepath, 'w') as file:
        file.write(contents)


def write_dataframe_to_file(df, filepath):
    """
    Writes pandas.DataFrame to a .csv file by its path.

    Args:
        df (DataFrame): DataFrame to be writen to a file.
        filepath (str): A path to a .csv file
    """
    if not isinstance(df, pd.DataFrame):
        print(f'Failed to write, because value of df argument is not pandas.DataFrame!')
        return

    df.to_csv(filepath)
