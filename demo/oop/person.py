class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return self.age

    # def __gt__(self, other):
    #     # print(self, other)
    #     return self.age > other.age


p1 = Person("Mike", 35)
p2 = Person("Mike", 30)
# print(p1)  # str(p1) ->  p1.__str__()
# print(p1 == p2)  # p1.__eq__(p2)
# print(p1 > p2)  # p1.__gt__(p2)
# print(p1 < p2)

# team = [Person('Jack', 30), Person('Jason', 25), Person('Billy', 22)]
# for p in sorted(team):
#     print(p)

team = {Person('Jack', 30), Person('Jack', 30), Person('Jason', 25),
        Person('Billy', 22)}

for p in team:
    print(p)

