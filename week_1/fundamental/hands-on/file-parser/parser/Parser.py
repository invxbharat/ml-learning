import json
import csv

from employee.Employee import Employee


class Parser:

    def parse_employee_json(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        employees = []

        for emp in data["employees"]:
            employee = Employee(
                emp["id"],
                emp["name"],
                emp["department"],
                emp["salary"],
                emp["age"],
                emp["city"]
            )

            employees.append(employee)

        return employees

    def parse_employee_csv(self, file_path):
        employees = []

        with open(file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for emp in reader:
                employee = Employee(
                    int(emp["id"]),
                    emp["name"],
                    emp["department"],
                    float(emp["salary"]),
                    int(emp["age"]),
                    emp["city"]
                )

                employees.append(employee)

        return employees

    def parse_file(self, file_path):
        if file_path.endswith(".json"):
            return self.parse_employee_json(file_path)

        elif file_path.endswith(".csv"):
            return self.parse_employee_csv(file_path)

        else:
            raise ValueError(
                "Unsupported file format. Please provide a JSON or CSV file."
            )
