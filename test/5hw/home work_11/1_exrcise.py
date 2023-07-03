class Company:
    def __init__(self, name, industry, headquarters, founder, year_founded):
        self.__name = name
        self.__industry = industry
        self.__headquarters = headquarters
        self.__founder = founder
        self.__year_founded = year_founded

    @property
    def name(self):
        return self.__name

    @property
    def industry(self):
        return self.__industry

    @property
    def headquarters(self):
        return self.__headquarters

    @property
    def founder(self):
        return self.__founder

    @property
    def year_founded(self):
        return self.__year_founded


toshiba = Company("Toshiba", "Electronics", "Tokyo, Japan", "Hisashige Tanaka", 1875)
apple = Company("Apple", "Technology", "Cupertino, California, United States",
                "Steve Jobs, Steve Wozniak, Ronald Wayne", 1976)

print(toshiba.name)
print(toshiba.industry)
print(toshiba.headquarters)
print(toshiba.founder)
print(toshiba.year_founded)

print(apple.name)
print(apple.industry)
print(apple.headquarters)
print(apple.founder)
print(apple.year_founded)
