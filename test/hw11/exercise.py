class Apple:
    def __init__(self, name: str, employees: int,country: str):
        self.name= name
        self.employees= employees
        self.country= country

if __name__=='__main__':
    company= Apple('Apple', 164000, 'USA')
print(f"""Name: {company.name}
Employees:{company.employees}
Country: {company.country}""")
