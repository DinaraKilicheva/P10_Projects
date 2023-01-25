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
        mode = "a"
        with open(file_path, mode, newline="\n") as f:
            csv_writer = csv.DictWriter(f, header)
            if mode == "w":
                csv_writer.writeheader()
            csv_writer.writerows(data)


csv_obj = CSVManager()
data_ = csv_obj.get_data_with_dict("List of most-followed Instagram accounts.csv")


def collect_data_by_country(row_data):
    grouped_by_country = {}
    for data in row_data:
        if data.get("Country/Continent") in grouped_by_country:
            grouped_by_country[data.get("Country/Continent")] = [*grouped_by_country[data.get("Country/Continent")],
                                                                 {"Rank": data.get("Rank"),
                                                                  "Username": data.get("Username"),
                                                                  "Owner": data.get("Owner"),
                                                                  "Followers(millions)[2]": data.get(
                                                                      "Followers(millions)[2]"),
                                                                  "Profession/Activity": data.get(
                                                                      "Profession/Activity"),
                                                                  "Country/Continent": data.get("Country/Continent")}]
        else:
            grouped_by_country[data.get("Country/Continent")] = [{"Rank": data.get("Rank"),
                                                                  "Username": data.get("Username"),
                                                                  "Owner": data.get("Owner"),
                                                                  "Followers(millions)[2]": data.get(
                                                                      "Followers(millions)[2]"),
                                                                  "Profession/Activity": data.get(
                                                                      "Profession/Activity"),
                                                                  "Country/Continent": data.get("Country/Continent")}]

    return grouped_by_country


country_list = collect_data_by_country(data_)
for key, value in country_list.items():
    header = ["Rank", "Username", "Owner", "Followers(millions)[2]", "Profession/Activity", "Country/Continent"]
    file_path = str(key)
    csv_obj.writer_with_dict(value, header, 'United States.csv')

print(country_list)
