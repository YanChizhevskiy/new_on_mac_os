from normal import *

school = School('MSU')

class1 = ClassRoom('1A')
class2 = ClassRoom('1B')
class3 = ClassRoom('2A')

teacher_one = Teacher('One', 'Teacher')
teacher_two = Teacher('Two', 'Teacher')

subject_maths = Subject('Math')
subject_maths.teacher = teacher_one

subject_program = Subject('Program')
subject_program.teacher = teacher_two

class1.teachers.append(teacher_one)
class1.teachers.append(teacher_two)
class2.teachers.append(teacher_two)
class3.teachers.append(teacher_one)

student1 = Student('Student', 'First')
student2 = Student('Student', 'Second')

parent1 = Parent('Father', 'First')
parent2 = Parent('Mother', 'First')

parent3 = Parent('Father', 'Second')
parent4 = Parent('Mother', 'Second')

student1.set_parents(parent1, parent2)
student2.set_parents(parent3, parent4)

class2.add_student(student1)
class2.add_student(student2)

all_classed = school.classrooms
print('1. All classes in school: ', all_classed)

class_students = class2.students
print('2. All students by class: ')
for x in class_students:
    print('\t', x)

students_subjects = [x.subject for x in student2.classroom.teachers]
print('3. Subject of student: ', students_subjects)

parents_names = [student2.father, student2.mother]
print('4. Student parents: ', parents_names)

class_teachers = class2.teachers
print("5. All teachers by class: ", class_teachers)