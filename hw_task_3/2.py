class EducationMaterials:
    def __init__(self, *args):
        self.materials = [*args]


class Student:
    def __init__(self):
        self.knowledge = []

    def take(self, new_knowledge):
        self.knowledge.append(new_knowledge)


class Teacher:
    def __init__(self):
        self.num_students = 0

    def teach(self, edu_mats, students: list[Student]):
        for student in students:
            student.take(edu_mats)
            self.num_students += 1


my_materials = EducationMaterials("Python", "Version Control Systems", "Relational Databases",
                                  "NoSQL databases", "Message Brokers")
my_teacher = Teacher()
student_list = [Student() for i in range(4)]

my_teacher.teach(my_materials.materials[0], student_list)
my_teacher.teach(my_materials.materials[1], [student_list[0], student_list[2]])
my_teacher.teach(my_materials.materials[2], student_list[2:3])
my_teacher.teach(my_materials.materials[3], student_list[1:2])
my_teacher.teach(my_materials.materials[4], [student_list[1], student_list[3]] )

for student in student_list:
    print(student.knowledge)
print(my_teacher.num_students)
