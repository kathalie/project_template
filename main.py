import app.io.input as i
import app.io.output as o


def main():
    output_text_file_name = './data/output.txt'
    output_csv_file_name = './data/output.csv'

    filepath = i.read_from_console('Enter a file path to read from: ')
    o.write_to_console(filepath)

    file_content = i.read_from_file(filepath)
    o.write_to_file(file_content, output_text_file_name)

    csv_filepath = i.read_from_console('Enter a .csv file path to read from: ')
    df = i.read_dataframe_from_file(csv_filepath)
    o.write_dataframe_to_file(df, output_csv_file_name)


if __name__ == '__main__':
    main()
