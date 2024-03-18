import pandas as pd

import app.io.output as o
import app.io.input as i


class TestWriteToFile:
    filename = 'tests/test_data/output.txt'

    def test_with_valid_content(self):
        valid_content = 'Hello, world!'
        success = o.write_to_file(valid_content, self.filename)
        read_content = i.read_from_file(self.filename)

        assert success
        assert read_content == valid_content

    def test_with_invalid_content(self):
        invalid_content = None
        success = o.write_to_file(invalid_content, self.filename)

        assert not success


class TestWriteDataframeToFile:
    filename = 'tests/test_data/output.csv'

    def test_with_valid_dataframe(self):
        valid_dataframe = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                           'mask': ['red', 'purple'],
                           'weapon': ['sai', 'bo staff']})
        success = o.write_dataframe_to_file(valid_dataframe, self.filename)
        read_dataframe = i.read_dataframe_from_file(self.filename)

        assert success
        assert read_dataframe.equals(valid_dataframe)

    def test_with_invalid_dataframe(self):
        invalid_dataframe = None
        success = o.write_dataframe_to_file(invalid_dataframe, self.filename)

        assert not success
