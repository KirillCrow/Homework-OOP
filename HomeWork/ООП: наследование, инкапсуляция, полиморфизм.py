class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached\
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Eror'

    def __average_grade(self, sum_grade=0, list_grade=0):
        for hw_grade in self.grades.values():
            list_grade += len(hw_grade)
            for all_grade in hw_grade:
                sum_grade += all_grade
            return sum_grade / list_grade
        else:
            return 'Eror'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашнее задание: {self.__average_grade()}\n' \
               f'Курсы в процессе изучения: {" ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {" ".join(self.finished_courses)}'

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise ValueError('Разные классы')
        return self.__average_grade() >= other.__average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise ValueError('Разные классы')
        return self.__average_grade() <= other.__average_grade()


def average_rating_stud(students, check_course, sum_grades=0, amount_grades=0):
    for i in range(len(all_students)):
        if check_course in all_students[i].finished_courses:
            amount_grades += len(all_students[i].grades.get(check_course))
            for grades in all_students[i].grades.get(check_course):
                sum_grades += grades
    return print(f'Средняя оценка по предмету {check_course}:'
                 f' {round(sum_grades / amount_grades, 2)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached\
                and course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def __average_grade(self, sum_grade=0, list_grade=0):
        for hw_grade in self.grades.values():
            list_grade += len(hw_grade)
            for all_grade in hw_grade:
                sum_grade += all_grade
            return sum_grade / list_grade
        else:
            return 'Eror'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.__average_grade()}'

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            raise ValueError('Разные классы')
        return self.__average_grade() >= other.__average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise ValueError('Разные классы')
        return self.__average_grade() <= other.__average_grade()


def average_rating_lect(lecturers, check_course, sum_grades=0, amount_grades=0):
    for i in range(len(all_lecturers)):
        if check_course in all_lecturers[i].courses_attached:
            amount_grades += len(all_lecturers[i].grades.get(check_course))
            for grades in all_lecturers[i].grades.get(check_course):
                sum_grades += grades
    return print(f'Средняя оценка преподавателей по предмету {check_course}:'
                 f' {round(sum_grades / amount_grades, 2)}')


first_student = Student('Andrew', 'Garfield')
first_student.finished_courses = ['Python', 'Git']
first_student.courses_in_progress = ['Data Science', 'JavaS']
second_student = Student('Tobey', 'Maguire')
second_student.finished_courses = ['Python', 'Git']
second_student.courses_in_progress = ['Data Science', 'JavaS']
all_students = [first_student, second_student]

first_reviewer = Reviewer('Otto', 'Octavius')
first_reviewer.courses_attached = ['Python']
second_reviewer = Reviewer('Norman', 'Osborn')
second_reviewer.courses_attached = ['Git']

first_lector = Lecturer('Tony', 'Stark')
first_lector.courses_attached = ['Data Science']
second_lector = Lecturer('Stephen', 'Strange')
second_lector.courses_attached = ['JavaS']
all_lecturers = [first_lector, second_lector]


first_student.rate_hw(first_lector, 'Data Science', 9)
first_student.rate_hw(second_lector, 'JavaS', 7)
second_student.rate_hw(first_lector, 'Data Science', 8)
second_student.rate_hw(second_lector, 'JavaS', 5)

first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(second_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Git', 5)
second_reviewer.rate_hw(second_student, 'Git', 9)

print('________________')
print(first_student)
print()
print(second_student)
print('________________')
print(first_lector)
print()
print(second_lector)
print('________________')
print(first_reviewer)
print()
print(second_reviewer)
print('________________')
print(first_student >= second_student)
print(first_student <= second_student)
print(first_lector >= second_lector)
print(first_lector <= second_lector)
print('________________')
average_rating_lect(all_lecturers, 'JavaS')
average_rating_lect(all_lecturers, 'Data Science')
average_rating_stud(all_students, 'Git')
average_rating_stud(all_students, 'Python')
