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
        return self.first_name + self.family_name

    def status(self):
        return self.first_name + self.family_name + str(self.age)


ken = Customer("Ken", "Tanaka", 15)
tom = Customer("Tom", "Ford", 57)
ieyasu = Customer("Iesasu", "Tokugawa", 73)

print(ken.status())
