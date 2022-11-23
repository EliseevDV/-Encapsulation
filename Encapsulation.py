class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.student_grades:
                lecturer.student_grades[course] += [grade]
            else:
                lecturer.student_grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        self.average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за Домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.student_grades = {}

    def average_rate(self):
        self.average = round(sum(sum(self.student_grades.values(), [])) / len(sum(self.student_grades.values(), [])), 1)
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_rate() < other.average_rate()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за лекции: {self.average_rate()} '
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"""Имя:{self.name}
Фамилия: {self.surname}"""

# def students_average( course_name, *students):
AnnaSt = Student('Анна', 'Кирилова', 'female')
DimaSt = Student('Дмитрий', 'Горбачев', 'Male')
AnnaSt.finished_courses += ['Введение в программирование']
AnnaSt.courses_in_progress += ['Python', 'Git']
DimaSt.finished_courses += ['Введение в программирование', 'GIT']
DimaSt.courses_in_progress += ['Python']


IgorMen = Mentor('Игорь', 'Сафронов')
InnaMen = Mentor('Инна', 'Кузнецова')


IvanLec = Lecturer('Иван', 'Кожушко')
NataliLec = Lecturer('Наталья', 'Заречная')
IvanLec.courses_attached += ['Python', 'Git']
NataliLec.courses_attached += ['Python', 'Git']

DenisLec = Reviewer('Денис', 'Зубенко')
SvetlanaRev = Reviewer('Светлана', 'Майорова')
DenisLec.courses_attached += ['Python', 'Git']
SvetlanaRev.courses_attached += ['Python', 'Git']


AnnaSt.rate_hw(IvanLec, 'Python', 9)
AnnaSt.rate_hw(NataliLec, 'Phython', 7)
DimaSt.rate_hw(IvanLec, 'Python', 10)
AnnaSt.rate_hw(NataliLec, 'Python', 9)
DimaSt.rate_hw(IvanLec, 'Python', 8)

DenisLec.rate_hw(AnnaSt, 'Python', 9)
DenisLec.rate_hw(DimaSt, 'Python', 10)
SvetlanaRev.rate_hw(AnnaSt, 'Python',10)
SvetlanaRev.rate_hw(AnnaSt, 'Python', 7)
SvetlanaRev.rate_hw(DimaSt, 'Python', 9)
DenisLec.rate_hw(AnnaSt, 'Git', 8)


AnnaSt.average_grade()
DimaSt.average_grade()
print(AnnaSt < DimaSt)
print(AnnaSt)
print(DimaSt)

IvanLec.average_rate()
NataliLec.average_rate()
print(IvanLec < NataliLec)
print(IvanLec)
print(NataliLec)

print(DenisLec)
print(SvetlanaRev)


student_list = [AnnaSt, DimaSt]


def grade_av_student(student_list, course):
    sum = 0
    count = 0
    for person in student_list:
        for i in person.grades[course]:
            sum += i
            count += 1
    return round(sum / count, 1)


lecturer_list = [IvanLec, NataliLec]


def grade_av_lecturer(lecturer_list, course):
    sum = 0
    count = 0
    for person in lecturer_list:
        for i in person.grades1[course]:
            sum += i
            count += 1
    return round(sum / count, 1)




