class Human:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

    def get_weight(self):
        print(self.weight)

    def get_height(self):
        print(self.height)

        
z = Human(name="Zafar",age="11",weight="42kg",height="152cm")
f = Human(name="Frank",age="56",weight="101kg",height="172cm")

print('Hi my name is', z.name, 'and I am', z.age, 'years old')
print('Hi my name is', f.name, 'and I am', f.age, 'years old')
