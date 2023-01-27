import csv


class CSVManager:

    @staticmethod
    def get_data_with_dict(file_path):
        try:
            with open(file_path) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                return [row for row in csv_reader]
        except FileNotFoundError as e:
            print(e)

    @staticmethod
    def writer_with_dict(data, header, file_path):

        with open(file_path, "w", newline="\n") as f:
            csv_writer = csv.DictWriter(f, header)
            csv_writer.writeheader()
            csv_writer.writerows(data)
