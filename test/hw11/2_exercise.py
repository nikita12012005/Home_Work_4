class Worker:
   def __init__(self, name: str, employee_id: int, position: str, department: str):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.department = department

if __name__== '__main__':
    vova= Worker('Vova', 4634974239, 'Senior Vice Presidents', 'United States Department of Justice')
    print(f"""Name: {vova.name}
Employee_id: {vova.employee_id}
Position: {vova.position} 
Department: {vova.department}""")
