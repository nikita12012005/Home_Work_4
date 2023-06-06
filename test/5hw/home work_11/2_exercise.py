class Worker:
    def __init__(self, name: str, employee_id: int,position: str, department: str):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.department = department

if __name__=='__main__':
    company= Worker('Dima', 164000, 'Senior Vice Presidents', 'Department of Justice')
print(f"""Name: {company.name}
Employee_id: {company.employee_id}
Position: {company.position}
Department: {company.department}""")