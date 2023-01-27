from module_3 import CSVManager

manager = CSVManager()

data_ = manager.get_data_with_dict("Most_Popular_Programming_Languages_from_2004_2022.csv")

def group_by_year(data):
    grouped_by_year = {}
    for row in data:
        year = row.get("Date").split(" ")[1]
        if year in grouped_by_year:
            grouped_by_year[year] = [*grouped_by_year[year], row]
        else:
            grouped_by_year[year] = [row]
    return grouped_by_year


print(group_by_year(data_))


def get_averages_by_year(datas):
    for key,value in datas.items():
        n=len(value)
        for dict in value:
            dict.pop("Date")
            for key,val in dict.items():







