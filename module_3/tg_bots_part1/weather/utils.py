import csv
import json
import os


def get_fullname(first_name, last_name):
    return f"{first_name} {last_name}" if last_name else first_name


def write_row_to_csv(file_path, header, row):
    with open(file_path, "a+", newline="\n") as f:
        csv_writer = csv.DictWriter(f, header)
        if os.path.getsize(file_path) == 0:
            csv_writer.writeheader()
        # csv_writer.writerow(student.get_attrs_for_csv_writer())
        csv_writer.writerow(row)
    print("Row add successfully.")


def write_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f)


def read_json(file_path):
    with open(file_path, "r") as f:
        result = json.load(f)
    return result

def get_weather_days(file_path):
    data=read_json(file_path)
    return [day_temp.get("day") for day_temp in data]