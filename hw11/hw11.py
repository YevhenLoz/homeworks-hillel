from abc import ABC, abstractmethod
from random import randint
from faker import Faker

fake = Faker()


class SchoolPersonnel(ABC):
    """
    Abstract Class School Personnel
    """

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def __str__(self):
        pass


class Teacher(SchoolPersonnel):
    """
    Class Teacher
    """

    def __str__(self):
        return f'Teacher {self.name}, {self.salary}'

    def __repr__(self):
        return f'Teacher {self.name}'


class Technician(SchoolPersonnel):
    """
    Class of technical personnel
    """

    def __str__(self):
        return f'Technician {self.name}, {self.salary}'

    def __repr__(self):
        return f'Teacher {self.name}'


class School:
    """
    This is class School
    """

    def __init__(self, school_name: str, school_principal: Teacher, number_of_teachers: int = 5,
                 number_of_technicians: int = 3):
        self.school_name = school_name
        self.principal = school_principal
        self.faculty = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
        self.teachers = [Teacher(fake.name(), randint(10000, 50000)) for _ in range(number_of_teachers)]
        self.technicians = [Technician(fake.name(), randint(3000, 6000)) for _ in range(number_of_technicians)]

    @property
    def assign_teacher_to_faculty(self):
        """
        This function appoints teacher to faculty
        """
        from random import shuffle
        all_teachers = [self.principal]
        all_teachers += self.teachers
        shuffle(all_teachers)
        shuffle(self.faculty)
        assignments = {faculty: all_teachers[i::len(self.faculty)]
                       for i, faculty in enumerate(self.faculty)}
        return assignments

    @property
    def school_total_salary(self):
        """
        This function returns total school salary
        :return: total
        """
        all_personnel = [self.principal]
        all_personnel += self.teachers
        all_personnel += self.technicians
        total = sum((obj.salary for obj in all_personnel))
        return total

    def appoint_new_principal(self):
        """
        This function appoints new principal and removes him from list of teachers
        Old principal is added to list of teachers
        """
        former_principal = self.principal
        candidate = self.teachers.pop()
        self.principal = candidate
        self.teachers.append(former_principal)


hogwarts = School('Hogwarts', Teacher('Albus Dumbledore', 100_000))
list_of_teachers = hogwarts.teachers
hogwarts_salary = hogwarts.school_total_salary
hogwarts.teachers.append(Teacher('Severus Snape', 90_000))
hogwarts_salary2 = hogwarts.school_total_salary
list_of_teachers2 = hogwarts.teachers
hogwarts.appoint_new_principal()
list_of_teachers3 = hogwarts.teachers
assign_to_faculty = hogwarts.assign_teacher_to_faculty
print()
