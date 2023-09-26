from random import randint

class Human:
    def __init__(self, name, age, male):
        self.name = name
        self.age = age
        self.male = male
        
        
class EducationMaterials:
    def __init__(self, *args):
        self.materials = [*args]

    def __len__(self):
        return len(self.materials)


class Student(Human):
    def __init__(self, name, age, male):
        super().__init__(name, age, male)
        self.knowledge = []

    def take(self, new_knowledge):
        self.knowledge.append(new_knowledge)

    def __len__(self):
        return len(self.knowledge)

    def forget(self):
        self.knowledge.pop(randint(0, len(self.knowledge) - 1))


class Teacher(Human):
    def __init__(self, name, age, male):
        super().__init__(name, age, male)
        self.num_students = 0

    def teach(self, edu_mats, students: list[Student]):
        for student in students:
            student.take(edu_mats)
            self.num_students += 1


my_materials = EducationMaterials("Python", "Version Control Systems", "Relational Databases",
                                  "NoSQL databases", "Message Brokers")
my_teacher = Teacher('Antonina Petrovna', 36, 'female')
student_list = [Student(f'Alex_{i}', 20, 'male') for i in range(4)]

my_teacher.teach(my_materials.materials[0], student_list)
my_teacher.teach(my_materials.materials[1], [student_list[0], student_list[2]])
my_teacher.teach(my_materials.materials[2], student_list[2:3])
my_teacher.teach(my_materials.materials[3], student_list[1:2])
my_teacher.teach(my_materials.materials[4], [student_list[1], student_list[3]])


print(len(my_materials))
for student in student_list:
    print(student.knowledge, len(student))
print(my_teacher.num_students)

for student in student_list:
    student.forget()
    print(student.knowledge, len(student))


