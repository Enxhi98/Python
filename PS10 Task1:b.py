class Student:
    def __init__(self, name="Enxhi", lastname="Kaziu", no=21321344, course="Computer Science with foundation"):
        self.name = name
        self.lastname = lastname
        self.no = no
        self.course = course


    def showDetails(self):
        print("Name:", self.name)
        print("Last name:", self.lastname)
        print("Student number:", self.no)
        print("Course:", self.course)



s0=Student()
s1=Student("Shirla" , "Preni" , 13459871 , "Economics")
s2=Student("Andja" , "Vllamasi" , 12345678 , "Engineering")
student = [s0, s1, s2]
for s in student:
    print()
    s.showDetails()


