class Student:
    courses = {'python': 5000, 'django': 3000, 'ds': 10000}

    @staticmethod
    def totalFee(course):
        return Student.courses[course.lower()]

    def __init__(self, name, course, feepaid=0):
        self.course = course.lower()
        if self.course not in Student.courses:
            raise ValueError('Invalid Course!')
        self.name = name
        self.feepaid = feepaid

    def payment(self, amount):
        self.feepaid += amount

    def due(self):
        return Student.courses[self.course] - self.feepaid


print(Student.totalFee('Django'))
s1 = Student("Mark", 'Python')
s1.payment(3000)
print(s1.due())
