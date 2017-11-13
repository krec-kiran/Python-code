from bank import Person

class School():

    def __init__(self, school_name):
        super().__init__()
        self.school_name = school_name

    def displaySchool(self):
        print("School name:", self.school_name)

# Teacher class inheriting from Person class


class Teacher(Person, School):

    def __init__(self, name, age, school_name):
        Person.__init__(self, name, age)
        School.__init__(self, school_name)


print("Primary school teachers are as follows.....")
primary_teachers = [Teacher('Mr Patrick', 45, "London Primary School")]
primary_teachers.append(
    Teacher('Miss Jones', 40, "Paddock Wood Primary School"))

for teachers in primary_teachers:
    teachers.show()
    teachers.displaySchool()


print("\n")

primary_teachers_staff = [{'name': "Mr A", 'age': 40, 'school': "ABCD"}, {
    'name': "Mr B", 'age': 30, 'school': "XYZ"}]

for staff in primary_teachers_staff:
    print(staff, "\n")

print("\n")
print("Secondary school teachers are as follows....")
secondary_teacher = Teacher('Miss Maynard', 38, "Judd Secondary School")
secondary_teacher.show()
secondary_teacher.displaySchool()

print("\n")
