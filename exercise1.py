class Human:
    number_of_eyes = 2

    def __init__(self, height: float, gender: str, name: str):
        self.height = height
        self.gender = gender
        self.name = name

    def sleep(self):
        print(f"{self.gender} Sleeping....")

    def eat(self):
        print("eating....")

    def __str__(self):
        return f"{self.name} {self.gender}"


h1 = Human(4.1, "male", "Emmanuel")
h2 = Human(3.5, "female", "Hannah")

print(h1.number_of_eyes)
print(h2.number_of_eyes)
print(h1.sleep())
print(h2.sleep())
print(h1)
print(h2)

print(type(h1))
