import csv


def get_data(file_path):
    try:
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            return [row for row in csv_reader]
    except FileNotFoundError as e:
        print(e)


data_ = get_data("countries of the world.csv")


def create_new_data(func):
    def replace(data):
        for country in data:
            for key, value in country.items():
                if "," in value:
                    country[key] = value.replace(",", ".")

        return func(data)

    return replace


@create_new_data
def writer_with_dict(data):
    header = list(data[0].keys())
    file_path = "result.csv"
    with open(file_path, "w", newline="\n", encoding="utf8") as f:
        csv_writer = csv.DictWriter(f, header)
        csv_writer.writeheader()
        csv_writer.writerows(data)


print(writer_with_dict(data_))
