class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

# print(student1.name)
# print(student1.age)
print(Student.num_students)
