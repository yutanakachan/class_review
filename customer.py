# ken = Customer(first_name="Ken", family_name="Tanaka")
# ken.full_name()  # "Ken Tanaka" という値を返す
# ​
# tom = Customer(first_name="Tom", family_name="Ford").full_name()
# tom.full_name()  # "Tom Ford" という値を返す

class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name},{self.family_name}"

    def status(self):
        return f"{self.full_name()},{str(self.age)}"

    def entry_fee(self):
        if self.age < 20:
            return 1000

        if self.age <= 20 and self.age < 65:
            return 1500

        if self.age >= 65:
            return 1200

    def info_csv(self):
        return f"{self.first_name},{self.family_name},{str(self.age)},{str(self.entry_fee())}"

ken = Customer("Ken", "Tanaka", 15)
tom = Customer("Tom", "Ford", 57)
ieyasu = Customer("Iesasu", "Tokugawa", 73)


print(ken.status())
print(ken.full_name())
