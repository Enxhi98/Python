class Student:
    def __init__(self, name="Enxhi", lastname="Kaziu", no=21321344, course="Computer Science with foundation"):
        self.name = name
        self.lastname = lastname
        self.no = no
        self.course = course

s = Student("Enxhi")
print("First name:" , s.name)
print("Last name:", s.lastname)
print("Student number/ID:", s.no)
print("Course:" , s.course)

