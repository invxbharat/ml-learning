from parser.Parser import Parser
from reports.Reports import Reports


parser = Parser()

# Parse CSV
employees = parser.parse_file("resource/employees.csv")


report = Reports()

report.generate_all_report(employees)

for employee in employees:
    print(
        employee.id,
        employee.name,
        employee.department,
        employee.salary,
        employee.age,
        employee.city
    )