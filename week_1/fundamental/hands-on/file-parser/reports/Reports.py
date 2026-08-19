class Reports:

    def get_employee_with_highest_salary(self, employees):
        if not employees:
            return None
        highest_salary_employee = max(employees, key=lambda emp: emp.salary)
        return highest_salary_employee

    def get_average_salary_by_department(self, employees):
        if not employees:
            return {}
        department_salaries = {}
        department_counts = {}
        for emp in employees:
            if emp.department not in department_salaries:
                department_salaries[emp.department] = 0
                department_counts[emp.department] = 0
            department_salaries[emp.department] += emp.salary
            department_counts[emp.department] += 1
        average_salaries = {dept: department_salaries[dept] / department_counts[dept]
                            for dept in department_salaries}
        return average_salaries

    def get_employee_count_by_city(self, employees):
        if not employees:
            return {}
        city_counts = {}
        for emp in employees:
            if emp.city not in city_counts:
                city_counts[emp.city] = 0
            city_counts[emp.city] += 1
        return city_counts

    def get_employee_count_by_age_group(self, employees):
        if not employees:
            return {}
        age_groups = {
            '20-29': 0,
            '30-39': 0,
            '40-49': 0,
            '50-59': 0,
            '60+': 0
        }
        for emp in employees:
            if 20 <= emp.age <= 29:
                age_groups['20-29'] += 1
            elif 30 <= emp.age <= 39:
                age_groups['30-39'] += 1
            elif 40 <= emp.age <= 49:
                age_groups['40-49'] += 1
            elif 50 <= emp.age <= 59:
                age_groups['50-59'] += 1
            elif emp.age >= 60:
                age_groups['60+'] += 1
        return age_groups

    # use match case

    def generate_report(self, employees, report_type):
        import csv
        from datetime import datetime

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{report_type}_report_{timestamp}.csv"

        match report_type:
            case "highest_salary":
                employee = self.get_employee_with_highest_salary(employees)
                if employee:
                    with open(filename, mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(["ID", "Name", "Department", "Salary", "Age", "City"])
                        writer.writerow([employee.id, employee.name, employee.department,
                                        employee.salary, employee.age, employee.city])
            case "average_salary_by_department":
                avg_salaries = self.get_average_salary_by_department(employees)
                with open(filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Department", "Average Salary"])
                    for dept, avg_salary in avg_salaries.items():
                        writer.writerow([dept, avg_salary])
            case "employee_count_by_city":
                city_counts = self.get_employee_count_by_city(employees)
                with open(filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["City", "Employee Count"])
                    for city, count in city_counts.items():
                        writer.writerow([city, count])
            case "employee_count_by_age_group":
                age_group_counts = self.get_employee_count_by_age_group(employees)
                with open(filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Age Group", "Employee Count"])
                    for age_group, count in age_group_counts.items():
                        writer.writerow([age_group, count])
            case _:
                raise ValueError("Unsupported report type. Please provide a valid report type.")


    def generate_all_report(self, employees):
        self.generate_report(employees, "highest_salary")
        self.generate_report(employees, "average_salary_by_department")
        print("---Reports generated successfully------")