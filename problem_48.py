class Ironman:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"Product: {self.name}, Price: {self.price}, Category: {self.category}")


class captain_america:
    def __init__(self, name, price, category, warranty_year):
        self.name = name
        self.price = price
        self.category = category
        self.warranty_year = warranty_year

    def get_info(self):
        print(f"Product: {self.name}, Price: {self.price}, Category: {self.category}, Warranty: {self.warranty_year}")


class hulk(Ironman, captain_america):
    def __init__(self, name, price, category, warranty_year, anger_issue):
        Ironman.__init__(self, name, price, category)
        captain_america.__init__(self, name, price, category, warranty_year)
        self.anger_issue = anger_issue

    def about(self):
        print(f"{self.name} costs {self.price}, category {self.category}, warranty till {self.warranty_year}, anger issue: {self.anger_issue}")


# Objects
hulk_1 = hulk("hulk", "1000", "Avengers", "2026", "yes")
captain = captain_america("captain_america", "1500", "Avengers", "2027")

print(hulk_1.anger_issue)
captain.get_info()