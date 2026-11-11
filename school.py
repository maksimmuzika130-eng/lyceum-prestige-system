class SchoolClass:
    def __init__(self, grade, letter):
        self.grade = int(grade)
        self.letter = letter
        self.students_list = []

    def get_class_name(self):
        return str(self.grade) + "-" + self.letter

    def add_student(self, student_obj):
        self.students_list.append(student_obj)

    def promote_to_next_grade(self):
        if self.grade >= 11:
            return False
        self.grade = self.grade + 1
        return True


class School:
    def __init__(self, name):
        self.name = name
        self.classes_list = []
        self.employees_list = []

    def add_class(self, class_obj):
        self.classes_list.append(class_obj)

    def add_employee(self, emp_obj):
        self.employees_list.append(emp_obj)

    def promote_all(self):
        still_in_school = []
        for c in self.classes_list:
            old_name = c.get_class_name()
            if c.promote_to_next_grade():
                still_in_school.append(c)
            else:
                print("🎓 Клас " + old_name + " успішно випустився!")
        self.classes_list = still_in_school