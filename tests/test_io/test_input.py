import app.io.input as i
import pandas as pd


class TestReadFromFile:
    def test_valid_data(self):
        filepath = 'tests/test_data/test.txt'
        file_content = 'Test'
        read_content = i.read_from_file(filepath)

        assert read_content == file_content

    def test_invalid_filepath(self):
        invalid_filepath = './nonexistent_file.txt'
        read_content = i.read_from_file(invalid_filepath)

        assert read_content is None

    def test_content_unchanged(self):
        filepath = 'tests/test_data/test.txt'
        read_content1 = i.read_from_file(filepath)
        read_content2 = i.read_from_file(filepath)

        assert read_content1 == read_content2


class TestReadFromFileUsingPandas:
    def test_valid_data(self):
        df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                           'mask': ['red', 'purple'],
                           'weapon': ['sai', 'bo staff']})
        filepath = 'tests/test_data/test.csv'
        read_df = i.read_dataframe_from_file(filepath)

        print(read_df)

        assert read_df.equals(df)

    def test_invalid_filepath(self):
        invalid_filepath = './nonexistent_file.csv'
        read_df = i.read_dataframe_from_file(invalid_filepath)

        assert read_df is None

    def test_content_unchanged(self):
        filepath = 'tests/test_data/test.csv'
        read_df1 = i.read_dataframe_from_file(filepath)
        read_df2 = i.read_dataframe_from_file(filepath)

        assert read_df1.equals(read_df2)

