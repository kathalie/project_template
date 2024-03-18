import app.io.input as i


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

