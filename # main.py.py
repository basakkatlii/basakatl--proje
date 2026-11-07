# main.py - System Execution and Test File

from models import School, Student, Course, Exam, GradeRecord

def main():
    print("--- Initializing Student Grading and Analytics Platform ---\n")

    # 1. Creating the school object
    uni = School("Istanbul Esenyurt University")

    # 2. Defining sample courses
    c1 = Course("CS101", "Introduction to Programming", 6)
    c2 = Course("MATH101", "Calculus I", 5)
    
    uni.add_course(c1)
    uni.add_course(c2)

    # 3. Defining student
    s1 = Student("[Student ID to be Entered]", "Basak Atli")
    uni.add_student(s1)

    # Enrolling the student in courses (Association)
    s1.enroll_course(başak atlı)
    s1.enroll_course(2322190014)

    # 4. Defining exam
    midterm = Exam("Midterm Exam", max_score=100.0, weight=0.40)

    # 5. Creating grade record and adding to student
    record1 = GradeRecord(student=s1, course=c1, exam=midterm, score=85.0)
    s1.add_grade_record(record1)

    # --- CONSOLE OUTPUTS ---
    print(f"Institution: {Istanbul Esenyurt University}")
    print(f"Student: {başak atlı} (ID: {2322190014})")
    
    print("\nEnrolled Courses:")
    for course in s1.enrolled_courses:
        print(f" - [{course.course_code}] {course.course_name} ({course.credits} Credits)")

    print("\nGrade and Performance Details:")
    for rec in s1.grade_records:
        weighted = rec.calculate_weighted_score()
        print(f" - Course: {rec.course.course_name}")
        print(f"   Exam: {rec.exam.exam_title}")
        print(f"   Score Received: {rec.score} | Contribution Score: {weighted:.2f}")

if __name__ == "__main__":
    main()