import csv


class CSVManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data(self):
        try:
            with open(self.file_path) as csv_file:
                csv_reader = csv.reader(csv_file)
                return [row for row in csv_reader]
        except (FileNotFoundError, UnicodeDecodeError) as e:
            print(e)

    def get_data_with_dict(self):
        try:
            with open(self.file_path) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                return [row for row in csv_reader]
        except (FileNotFoundError, UnicodeDecodeError) as e:
            print(e)

    def get_language_info(self, programming_lang):
        """
        # Python
        # Avgust 2004: 30
        # Avgust 2005: 31
        # Avgust 2006: 32
        :param programming_lang:
        :return:
        """
        data = self.get_data()
        header = [item.lower() for item in data.pop(0)]
        if programming_lang.lower() not in header:
            return "Language not found."

        target_index = None
        for index, item in enumerate(header):
            if programming_lang == item:
                target_index = index

        result = f"{programming_lang.title()}\n"
        for row in data:
            result += f"{row[0]}: {row[target_index]}\n"

        return result

    def get_language_info_with_dict(self, programming_lang):
        data = self.get_data_with_dict()
        for row in data:
            print("row", row.get(programming_lang))

    def writer(self, data):
        with open(self.file_path, "w") as f:
            csv_writer = csv.writer(f)
            # csv_writer.writerows(data)
            for row in data:
                csv_writer.writerow(row)

    def writer_with_dict(self, data, header):
        mode = "a"
        with open(self.file_path, mode, newline="\n") as f:
            csv_writer = csv.DictWriter(f, header)
            if mode == "w":
                csv_writer.writeheader()
            csv_writer.writerows(data)


csv_obj = CSVManager("../csv_files/Most Popular Programming Languages from 2004 to 2022.csv")
# print(csv_obj.get_language_info("java"))
# csv_obj.get_language_info_with_dict("Python")

csv_obj2 = CSVManager("../csv_files/test.csv")

# test_data = [
#     ["id", "name", "age"],
#     [123, "A", 20],
#     [124, "B", 21],
#     [125, "C", 22]
# ]
# csv_obj2.writer(test_data)

column_names = ["id", "name", "age"]
test_data = [
    {
        "id": 123,
        "age": 20,
        "name": "A"
    },
    {
        "name": "B",
        "id": 124,
        "age": 21
    },
    {
        "id": 125,
        "name": "C",
        "age": 22
    }
]

csv_obj2.writer_with_dict(test_data, column_names)


def group_by_year(data):
    grouped_by_year = {}
    for lang in data:
        year = lang.get("Date").split(" ")[1]
        if year in grouped_by_year:
            grouped_by_year[lang.get("Date").split(" ")[1]] = [*grouped_by_year[lang.get("Date").split(" ")[1]],
                                                               {"Abap": lang.get("Abap"), "Ada": lang.get("Ada"),
                                                                "C/C++": lang.get("C/C++"), "C#": lang.get("C#"),
                                                                "Cobol": lang.get("Cobol"), "Dart": lang.get("Dart"),
                                                                "Delphi/Pascal": lang.get("Delphi/Pascal"),
                                                                "Go": lang.get("Go"), "Groovy": lang.get("Groovy"),
                                                                "Haskell": lang.get("Haskell"),
                                                                "Java": lang.get("Java"),
                                                                "JavaScript": lang.get("JavaScript"),
                                                                "Julia": lang.get("Julia"), "Kotlin": lang.get(
                                                                   "Kotlin"), "Lua": lang.get("Lua"),
                                                                "Matlab": lang.get("Matlab"),
                                                                "Objective-C": lang.get("Objective-C"),
                                                                "Perl": lang.get("Perl"), "PHP": lang.get("PHP"),
                                                                "Python": lang.get("Python"), "R": lang.get("R"),
                                                                "Ruby": lang.get("Ruby"), "Rust": lang.get(
                                                                   "Rust"), "Scala": lang.get("Scala"),
                                                                "Swift": lang.get("Swift"),
                                                                "TypeScript": lang.get("TypeScript"),
                                                                "VBA": lang.get("VBA"),
                                                                "Visual Basic": lang.get("Visual Basic")}]
        else:
            grouped_by_year[lang.get("Date").split(" ")[1]] = [
                {"Abap": lang.get("Abap"), "Ada": lang.get("Ada"), "C/C++": lang.get("C/C++"), "C#": lang.get("C#"),
                 "Cobol": lang.get("Cobol"), "Dart": lang.get("Dart"), "Delphi/Pascal": lang.get("Delphi/Pascal"),
                 "Go": lang.get("Go"), "Groovy": lang.get("Groovy"),
                 "Haskell": lang.get("Haskell"), "Java": lang.get("Java"),
                 "JavaScript": lang.get("JavaScript"), "Julia": lang.get("Julia"), "Kotlin": lang.get(
                    "Kotlin"), "Lua": lang.get("Lua"), "Matlab": lang.get("Matlab"),
                 "Objective-C": lang.get("Objective-C"), "Perl": lang.get("Perl"), "PHP": lang.get("PHP"),
                 "Python": lang.get("Python"), "R": lang.get("R"), "Ruby": lang.get("Ruby"), "Rust": lang.get(
                    "Rust"), "Scala": lang.get("Scala"), "Swift": lang.get("Swift"),
                 "TypeScript": lang.get("TypeScript"), "VBA": lang.get("VBA"),
                 "Visual Basic": lang.get("Visual Basic")}
            ]

        print(grouped_by_year())
