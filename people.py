class Student:
    def __init__(self, last_name, first_name, middle_name, birth_year, gender, average_grade):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.birth_year = int(birth_year)
        self.gender = gender # 'Х' або 'Д'
        self.average_grade = float(average_grade)

    def get_full_name(self):
        return self.last_name + " " + self.first_name + " " + self.middle_name


class Employee:
    def __init__(self, full_name, base_salary):
        self.full_name = full_name
        self.base_salary = float(base_salary)

    def calculate_salary(self):
        return self.base_salary


class Director(Employee):
    def __init__(self, full_name, base_salary, ped_exp, mng_exp):
        super().__init__(full_name, base_salary)
        self.ped_exp = int(ped_exp)
        self.mng_exp = int(mng_exp)

    def calculate_salary(self):
        return (self.base_salary * self.ped_exp / 50) + (self.mng_exp * 500)


class Teacher(Employee):
    def __init__(self, full_name, base_salary, ped_exp):
        super().__init__(full_name, base_salary)
        self.ped_exp = int(ped_exp)

    def calculate_salary(self):
        return self.base_salary * self.ped_exp / 30


class Guard(Employee):
    def __init__(self, full_name, base_salary, total_exp):
        super().__init__(full_name, base_salary)
        self.total_exp = int(total_exp)

    def calculate_salary(self):
        return self.base_salary + (self.total_exp * 250)