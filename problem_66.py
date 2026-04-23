#student grde system
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        else:
            return "C"


s = Student("Rahul", [80, 90, 85])
print(s.average())
print(s.grade())