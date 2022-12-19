class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        self.salary = salary
        self.courses = {}
        SchoolMember.__init__(self, name, age)

    def addCourse(self, signature, name):
        self.courses.update({signature: name})

    def getCourses(self):
        for key, value in self.courses.items():
            print(key, value)

    def getSalary(self):
        return self.salary


class Student(SchoolMember):
    def __init__(self, name, age):
        self.marks = {}
        self.courses = {}
        SchoolMember.__init__(self, name, age)

    def attendCourse(self, signature, year):
        self.courses.update({signature: year})

    def addGrade(self, signature, mark):
        if signature in self.marks:
            self.marks[signature] += [mark]
        else:
            self.marks[signature] = [mark]

    def getAvgGrade(self, signature):
        return sum(self.marks.get(signature)) / len(self.marks.get(signature))

    def getCourses(self):
        print(self.marks)
        for key, value in self.courses.items():
            print(key + " {'grade': " + str(self.marks.get(key)) + ", 'year':" + str(self.courses.get(key)) + "}")