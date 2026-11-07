# Stage 01 Report: Architectural Design and Core Implementation

*Course:* Object-based programming  
*University:* Istanbul Esenyurt University  
*Student Full Name:* Başak Atlı 
*Student ID:* [2322190014]  
*Project Name:* Student Grading and Analytics Platform  

---

## 1. Introduction and Objectives
The primary objective of this first stage (Stage 1) is to establish a sustainable and flexible software architecture complying with Object-Oriented Programming (OOP) principles for the Student Grading and Analytics Platform system. Throughout the project process, modular class structures were designed, and GitHub was chosen as the version control system.

## 2. Architecture and Class Design
The system is built upon 5 main classes:
1. *School*: Represents the institution; lists the students enrolled and courses offered within.
2. *Student*: Tracks the student profiles in the system, enrolled courses, and exam grades.
3. *Course*: Defines the code, name, and credit value of academic courses.
4. *Exam*: Determines the impact ratio (weight) and maximum score scale of exams.
5. *GradeRecord*: Dynamically calculates the weighted grade by connecting student, course, and exam objects.

## 3. Applied OOP Principles
- *Encapsulation:* Data belonging to an object and the methods operating on that data are logically encapsulated within their respective classes.
- *Association & Composition:* Classes are modeled to communicate via references using "Has-A" relationships.

## 4. AI Usage Disclosure
Academic Disclosure: Technical support was obtained from artificial intelligence language models during the architectural design of this project, the organization of the file hierarchy, and the preparation of documentation drafts.