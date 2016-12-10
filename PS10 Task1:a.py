class Student:
    def __init__(self, name="Enxhi", lastname="Kaziu", no=21321344, course="Computer Science with foundation"):
        self.name = name
        self.lastname = lastname
        self.no = no
        self.course = course

    def showDetails(self):
        print("\nFirst name:" , self.name)
        print("\Last name:" , self.lastname)
        print("\Student number:" , self.no)
        print("\Course:" , self.course)


    
s = Student("Enxhi")
print(s.name)
print(s.lastname)
print(s.no)
print(s.course)


