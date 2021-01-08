class Human:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height


z = Human(name="Zafar",age=11,weight=42,height=152)
f = Human(name="Frank",age=56,weight=101,height=172)

print('Hi my name is', z.name, 'and I am', z.age, 'years old')
print('Hi my name is', f.name, 'and I am', f.age, 'years old')
