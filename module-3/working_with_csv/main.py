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
    def writer_with_dict(data_csv, header_scv, file_path):
        with open(file_path, "w",newline="\n") as f:
            csv_writer = csv.DictWriter(f, header_scv)
            csv_writer.writeheader()
            csv_writer.writerows(data_csv)


csv_obj = CSVManager()
department_info = csv_obj.get_data_with_dict("Department_Information.csv")
employee_info = csv_obj.get_data_with_dict("Employee_Information.csv")
header = ["Employee ID", "DOB", "DOJ", "Department_Name"]


def merge_employee_department_by_ID(department, employee):
    result = []
    for emp in employee:
        for dept in department:
            if emp["Department_ID"] == dept["Department_ID"]:
                result.append({'Employee ID': emp.get("Employee ID"), 'DOB': emp.get("DOB"), 'DOJ': emp.get("DOJ"),
                               'Department_Name': dept.get("Department_Name")})
    return result


data = merge_employee_department_by_ID(department_info, employee_info)

csv_obj.writer_with_dict(data, header, "result.csv")
