class Company:
    class Employee:
        def __init__(self, name, position) -> None:
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        pass


company = Company("Krusty Krab")


class Employee:
    print("This is the second class")
