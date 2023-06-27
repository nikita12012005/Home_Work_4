class Company:
    def __init__(self, name, industry, headquarters, founder, year_founded):
        self.name = name
        self.industry = industry
        self.headquarters = headquarters
        self.founder = founder
        self.year_founded = year_founded

    def get_name(self):
        return self.name

    def get_industry(self):
        return self.industry

    def get_headquarters(self):
        return self.headquarters

    def get_founder(self):
        return self.founder

    def get_year_founded(self):
        return self.year_founded

    def set_name(self, name):
        self.name = name

    def set_industry(self, industry):
        self.industry = industry

    def set_headquarters(self, headquarters):
        self.headquarters = headquarters

    def set_founder(self, founder):
        self.founder = founder

    def set_year_founded(self, year_founded):
        self.year_founded = year_founded


toshiba = Company("Toshiba", "Electronics", "Tokyo, Japan", "Hisashige Tanaka", 1875)
apple = Company("Apple", "Technology", "Cupertino, California, United States", "Steve Jobs, Steve Wozniak, Ronald Wayne", 1976)

print(toshiba.get_name())
print(toshiba.get_industry())
print(toshiba.get_headquarters())
print(toshiba.get_founder())
print(toshiba.get_year_founded())

print(apple.get_name())
print(apple.get_industry())
print(apple.get_headquarters())
print(apple.get_founder())
print(apple.get_year_founded())

