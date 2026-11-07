# models.py - OOP Sınıf Tanımları

class School:
    def _init_(self, name: str):
        self.name = name
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)


class Student:
    def _init_(self, student_id: str, full_name: str):
        self.student_id = student_id
        self.full_name = full_name
        self.enrolled_courses = []
        self.grade_records = []

    def enroll_course(self, course):
        self.enrolled_courses.append(course)

    def add_grade_record(self, record):
        self.grade_records.append(record)


class Course:
    def _init_(self, course_code: str, course_name: str, credits: int):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits


class Exam:
    def _init_(self, exam_title: str, max_score: float, weight: float):
        self.exam_title = exam_title
        self.max_score = max_score
        self.weight = weight  # Örn: 0.40 (Vize etkisi %40)


class GradeRecord:
    def _init_(self, student: Student, course: Course, exam: Exam, score: float):
        self.student = student
        self.course = course
        self.exam = exam
        self.score = score

    def calculate_weighted_score(self) -> float:
        # Alınan notu ağırlıklı nota çeviren OOP metodu
        return (self.score / self.exam.max_score) * (self.exam.weight * 100)
    